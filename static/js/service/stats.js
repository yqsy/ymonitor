ymonitorApp.service('YmonitorStats', function ($rootScope, $q, $http, $timeout) {

    var _data = false;

    this.getData = function () {
        return _data;
    }

    this.init = function () {
        var refreshData = function () {
            return $q.all([
                getCpuStats(),
                getMemStats(),
                getDiskStats(),
                getNetStats()
            ]).then(function (results) {
                _data = {
                    'cpu_stats': results[0],
                    'mem_stats': results[1],
                    'disk_stats': results[2],
                    'net_stats': results[3]
                };
                $rootScope.$broadcast('data_refreshed', _data);
                nextLoad();
            }, function (reason) {
                $rootScope.$broadcast('is_disconnected');
                nextLoad();
            });
        };

        var loadPromise;

        var cancelNextLoad = function () {
          $timeout.cancel(loadPromise);
        };

        var nextLoad = function () {
          cancelNextLoad();
          loadPromise = $timeout(refreshData, 1000);
        };

        refreshData();
    };

    var getCpuStats = function () {
        return $http.get('api/cpu').then(function (response) {
            return response.data;
        });
    };

    var getMemStats = function () {
        return  $http.get('api/mem').then(function (response) {
            return response.data;
        });
    };

    var getDiskStats = function () {
        return  $http.get('api/diskio').then(function (response) {
            return response.data;
        });
    };

    var getNetStats = function () {
        return  $http.get('api/netio').then(function (response) {
            return response.data;
        });
    };
});