var ymonitorApp = angular.module('ymonitorApp', []);


ymonitorApp.run(function (YmonitorStats) {
    YmonitorStats.init();
});


ymonitorApp.controller('cpu', function ($scope, YmonitorStats) {

    $scope.$on('data_refreshed', function (event, data) {

        $scope.barwidth = 50;
    });

});


