var pollsApp = angular.module('pollsApp', []);

pollsApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[')
    .endSymbol(']]');
});

pollsApp.controller('UserPollCtrl', function($scope, $http) {

    // Get the Poll
    $scope.poll = ""

    $http.get('/api/v1/polls/1').
        success(function(data) {
            $scope.poll = data;
        }).
        error(function(data, status) {
            console.log("calling /api/v1/polls/1 returned status " + status);
        });

    $scope.total_votes = 0;

    $scope.vote = function(item) {
        item.votes += 1;
        $http.put('/api/v1/poll_items/'+item.id, item).
            success(function(data) {
                $http.get('/api/v1/polls/1').success(function(data) {
                    $scope.poll = data;
                }).
                error(function(data, status) {
                    console.log("calling /api/v1/polls/1 returned status " +
                                status);
                });
            }).
            error(function(data, status) {
                console.log("calling PUT /api/v1/poll_items returned status " +
                            status);
            });
    };

    $scope.barcolor = function(i) {
        colors = ['progress-bar-success', 'progress-bar-info',
            'progress-bar-warning', 'progress-bar-danger', '']
        idx = i % colors.length;
        return colors[idx];
    };
});

