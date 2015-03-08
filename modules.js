var myModule = angular.module('sprinter',[]);


myModule.factory('jiraRepo',function($http){
	return {
		getAllBoards: function (){
			var url = "http://127.0.0.1:5000/scrumBoard";
			return $http.get(url);
		},
		getBoardTickets:function(boardId) {
			var url = "http://127.0.0.1:5000/tickets/"+boardId;
			return $http.get(url);
		},
		getAllRepos:function(){
			var url = "http://127.0.0.1:5000/repos";
			return $http.get(url);
		},
		createBranch:function(data) {
			var url = "http://127.0.0.1:5000/branches";
			return $http.post(url,data);
		}
	};
});

myModule.controller('myController',function($scope,jiraRepo){
	$scope.firstName = "Shreyas";
	$scope.boardSelectedFlag = false;
	$scope.tempScope = [];

	$scope.boardSelected = function(){
		$scope.boardSelectedFlag = true;
		jiraRepo.getBoardTickets($scope.selectedScrumBoard).success(function(data){
			$scope.scrumTickets=data;	
		})
	};


	$scope.createBranches = function(){
		for (var i = $scope.scrumTickets.length - 1; i >= 0; i--) {
			var tempObj = $scope.scrumTickets[i];
			if (tempObj.branch == null) {
				alert("Select branch for Ticket Id "+tempObj.id);
				return;
			}
		};

		// Make an API call for making a branch and also the jenkins job
		jiraRepo.createBranch($scope.scrumTickets).success(function(){
			alert("Branches and jobs created successfully !!");
		});
	};

	$scope.updateItemScope = function(item,selectedBranch) {
		$scope.scrumTickets[item]["branch"] = selectedBranch;
		//console.log($scope.scrumTickets[item])
	};

	jiraRepo.getAllBoards().success(function(data){
		$scope.scrumBoards = data;
	});

	jiraRepo.getAllRepos().success(function(data){
		$scope.repoList = data;
	});
});