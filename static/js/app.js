var ymonitorApp = angular.module('ymonitorApp', []);


ymonitorApp.run(function (YmonitorStats) {
    YmonitorStats.init();
});


ymonitorApp.controller('cpu', function ($scope, YmonitorStats) {

    $scope.$on('data_refreshed', function (event, data) {

        $scope.barwidth = data['cpu_stats']['stat']['used_percent'];
    });

});


ymonitorApp.controller('mem', function ($scope, YmonitorStats) {

    $scope.$on('data_refreshed', function (event, data) {

        $scope.$on('data_refreshed', function(event,data){
          $scope.barwidth = data['mem_stats']['stat']['used_percent'];
        })
    });

});


ymonitorApp.controller('diskio', function ($scope, YmonitorStats) {

    $scope.$on('data_refreshed', function (event, data) {

        // $scope.barwidth = 50;
    });

});


ymonitorApp.controller('netio', function ($scope, YmonitorStats) {

    $scope.$on('data_refreshed', function (event, data) {

        // $scope.barwidth = 50;
    });

});
