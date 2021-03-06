import ArchiveManagerCtrl from '../controllers/ArchiveManagerCtrl';

export default {
  templateUrl: 'static/frontend/views/archive_manager.html',
  controller: [
    '$scope',
    '$http',
    'appConfig',
    '$uibModal',
    '$log',
    '$state',
    '$stateParams',
    'myService',
    'listViewService',
    '$translate',
    '$transitions',
    ArchiveManagerCtrl,
  ],
  controllerAs: 'vm',
  bindings: {},
};
