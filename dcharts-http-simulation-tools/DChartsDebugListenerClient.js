//relies on presence of jquery

DChartsDebugListenerClient = function(){

	this.onEntry = function(state){
		//console.log("Entering ",state);
		jQuery.post("/",{stateid:state,command:"enter"})
	}

	this.onExit = function(state){
		//console.log("Exiting ",state);
		jQuery.post("/",{stateid:state,command:"exit"})
	}

	this.onTransition = function(sourceStateId,targetStateId,transition){
		//TODO
	}
}
