import mock

from mytwitter.cmd import api
from mytwitter.tests import base

class TestApiCmd(base.BaseTestCase):

    @mock.patch.object(api.parser, 'parse_args')
    @mock.patch.object(api, 'CONF')
    @mock.patch.object(api.log, 'configure_logging')
    @mock.patch.object(api.api.app, 'run')
    def test_main(self, mock_run, mock_configure_logging, mock_CONF, mock_parse_args):
        #setup.
        mock_args = mock.Mock()
        mock_parse_args.return_value = mock_args
        mock_CONF.api.port = 11111

        #the call itself.
        api.main()

        #the expectations / asserts.
        mock_parse_args.assert_called_once_with()
        mock_CONF.load_config.assert_called_once_with(mock_args.config_path)
        mock_run.assert_called_once_with(
            host='0.0.0.0', port=mock_CONF.api.port)