function ClientBehaviourStatechartExecutionContext() {
    var self = this; //used in the rare occasions we call public functions from inside this class
    //system variable declarations
    var _event = {
        name: undefined,
        data: undefined
    },
        _name = "ClientBehaviour",
        _sessionid;
    var _x = {
        _event: _event,
        _name: _name,
        _sessionid: _sessionid
    };
    //variable declarations relating to data model
    var ext, scInstance;
    //send timeout id variables
    var $default_Regexp_id2610855 = /^($default)/,
        init_Regexp_id2610861 = /^(init)/,
        play_Regexp_id2610867 = /^(play)/,
        stop_Regexp_id2610873 = /^(stop)/,
        reset_Regexp_id2610878 = /^(reset)/,
        pause_Regexp_id2610884 = /^(pause)/,
        send_event_Regexp_id2610890 = /^(send_event)/;
    //abstract state
    var AbstractState = new
    function() {
        //triggers are methods
        this.$default = function() {};
        this.init = function() {};
        this.play = function() {};
        this.pause = function() {};
        this.send_event = function() {};
        this.stop = function() {};
        this.reset = function() {};
        this.$default = function() {};
        this.$dispatchPrefixEvent = function() {};
    }
    //states
    var scxml_id2608018 = (function() {
        function scxml_id2608018Constructor() {
            this.parent = AbstractState;
            this.initial = null;
            this.depth = 0;
            this.historyState = null;
            //these variables facilitate fast In predicate
            this.isBasic =
            false;
            this.toString = function() {
                return "scxml_id2608018"
            }
            this.enterAction = function() {
                for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                id2607964_iterator < id2607964_hoist;
                id2607964_iterator++) {
                    var listener = listeners[id2607964_iterator];
                    //to
                    listener.onEntry("scxml_id2608018");
                }
            }
            this.exitAction = function() {
                for (var id2608545_iterator = 0, id2608545_hoist = listeners.length;
                id2608545_iterator < id2608545_hoist;
                id2608545_iterator++) {
                    var listener = listeners[id2608545_iterator];
                    //from
                    listener.onExit("scxml_id2608018");
                }
            }
            this.$dispatchPrefixEvent = function(e) {
                return AbstractState.$dispatchPrefixEvent(e);
            }
        }
        scxml_id2608018Constructor.prototype = AbstractState;
        return new scxml_id2608018Constructor();
    })();
    var _initial = (function() {
        function _initialConstructor() {
            this.parent = scxml_id2608018;
            this.initial = null;
            this.depth = 1;
            this.historyState = null;
            //these variables facilitate fast In predicate
            this.isBasic =
            true;
            this.ancestors = [
            scxml_id2608018];
            this.parent.initial = this; //init parent's pointer to initial state
            this.toString = function() {
                return "_initial"
            }
            this.enterAction = function() {
                for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                id2607964_iterator < id2607964_hoist;
                id2607964_iterator++) {
                    var listener = listeners[id2607964_iterator];
                    //to
                    listener.onEntry("_initial");
                }
            }
            this.exitAction = function() {
                for (var id2608832_iterator = 0, id2608832_hoist = listeners.length;
                id2608832_iterator < id2608832_hoist;
                id2608832_iterator++) {
                    var listener = listeners[id2608832_iterator];
                    //from
                    listener.onExit("_initial");
                }
            }
            this.$default = function() {
                return {
                    preemptedBasicStates: {
                        initial_default: true,
                        stopped: true,
                        paused: true,
                        running: true
                    },
                    action: function() {
                        hasTakenDefaultTransition = true;
                        //exit states
                        _initial.exitAction();
                        //transition action
                        for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var listener = listeners[id2607964_iterator];
                            //transition id
                            listener.onTransition("", "initial_default", "_initial_$default_1");
                        }
                        //enter states
                        initial_default.enterAction();
                        //update configuration
                        currentConfiguration = [
                        initial_default];
                    }
                }
                return scxml_id2608018['$default']();
            }
            this.$dispatchPrefixEvent = function(e) {
                return scxml_id2608018.$dispatchPrefixEvent(e);
            }
        }
        _initialConstructor.prototype = scxml_id2608018;
        return new _initialConstructor();
    })();
    var initial_default = (function() {
        function initial_defaultConstructor() {
            this.parent = scxml_id2608018;
            this.initial = null;
            this.depth = 1;
            this.historyState = null;
            //these variables facilitate fast In predicate
            this.isBasic =
            true;
            this.ancestors = [
            scxml_id2608018];
            this.toString = function() {
                return "initial_default"
            }
            this.enterAction = function() {
                for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                id2607964_iterator < id2607964_hoist;
                id2607964_iterator++) {
                    var listener = listeners[id2607964_iterator];
                    //to
                    listener.onEntry("initial_default");
                }
            }
            this.exitAction = function() {
                for (var id2609490_iterator = 0, id2609490_hoist = listeners.length;
                id2609490_iterator < id2609490_hoist;
                id2609490_iterator++) {
                    var listener = listeners[id2609490_iterator];
                    //from
                    listener.onExit("initial_default");
                }
            }
            this.init = function() {
                return {
                    preemptedBasicStates: {
                        initial_default: true,
                        stopped: true,
                        paused: true,
                        running: true
                    },
                    action: function() {
                        //exit states
                        initial_default.exitAction();
                        //transition action
                        ext = _event.data;
                        for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var listener = listeners[id2607964_iterator];
                            //transition id
                            listener.onTransition("", "stopped", "initial_default_init_2");
                        }
                        //enter states
                        stopped.enterAction();
                        //update configuration
                        currentConfiguration = [
                        stopped];
                    }
                }
                return scxml_id2608018['init']();
            }
            this.$dispatchPrefixEvent = function(e) {
                if (e.match(init_Regexp_id2610861)) {
                    return {
                        preemptedBasicStates: {
                            initial_default: true,
                            stopped: true,
                            paused: true,
                            running: true
                        },
                        action: function() {
                            //exit states
                            initial_default.exitAction();
                            //transition action
                            ext = _event.data;
                            for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var listener = listeners[id2607964_iterator];
                                //transition id
                                listener.onTransition("initial_default", "stopped", "initial_default_init_2");
                            }
                            //enter states
                            stopped.enterAction();
                            //update configuration
                            currentConfiguration = [
                            stopped];
                        }
                    }
                }
                return scxml_id2608018.$dispatchPrefixEvent(e);
            }
        }
        initial_defaultConstructor.prototype = scxml_id2608018;
        return new initial_defaultConstructor();
    })();
    var stopped = (function() {
        function stoppedConstructor() {
            this.parent = scxml_id2608018;
            this.initial = null;
            this.depth = 1;
            this.historyState = null;
            //these variables facilitate fast In predicate
            this.isBasic =
            true;
            this.ancestors = [
            scxml_id2608018];
            this.toString = function() {
                return "stopped"
            }
            this.enterAction = function() {
                enable(ext.playButton);
                disable(ext.pauseButton);
                disable(ext.resetButton);
                disable(ext.stopButton);
                for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                id2607964_iterator < id2607964_hoist;
                id2607964_iterator++) {
                    var listener = listeners[id2607964_iterator];
                    //to
                    listener.onEntry("stopped");
                }
            }
            this.exitAction = function() {
                for (var id2608504_iterator = 0, id2608504_hoist = listeners.length;
                id2608504_iterator < id2608504_hoist;
                id2608504_iterator++) {
                    var listener = listeners[id2608504_iterator];
                    //from
                    listener.onExit("stopped");
                }
            }
            this.play = function() {
                return {
                    preemptedBasicStates: {
                        initial_default: true,
                        stopped: true,
                        paused: true,
                        running: true
                    },
                    action: function() {
                        //exit states
                        stopped.exitAction();
                        //transition action
                        for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var listener = listeners[id2607964_iterator];
                            //transition id
                            listener.onTransition("", "started_initial", "stopped_play_3");
                        }
                        //enter states
                        started.enterAction();
                        started_initial.enterAction();
                        //update configuration
                        currentConfiguration = [
                        started_initial];
                    }
                }
                return scxml_id2608018['play']();
            }
            this.$dispatchPrefixEvent = function(e) {
                if (e.match(play_Regexp_id2610867)) {
                    return {
                        preemptedBasicStates: {
                            initial_default: true,
                            stopped: true,
                            paused: true,
                            running: true
                        },
                        action: function() {
                            //exit states
                            stopped.exitAction();
                            //transition action
                            for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var listener = listeners[id2607964_iterator];
                                //transition id
                                listener.onTransition("stopped", "started_initial", "stopped_play_3");
                            }
                            //enter states
                            started.enterAction();
                            started_initial.enterAction();
                            //update configuration
                            currentConfiguration = [
                            started_initial];
                        }
                    }
                }
                return scxml_id2608018.$dispatchPrefixEvent(e);
            }
        }
        stoppedConstructor.prototype = scxml_id2608018;
        return new stoppedConstructor();
    })();
    var started = (function() {
        function startedConstructor() {
            this.parent = scxml_id2608018;
            this.initial = null;
            this.depth = 1;
            this.historyState = null;
            //these variables facilitate fast In predicate
            this.isBasic =
            false;
            this.toString = function() {
                return "started"
            }
            this.enterAction = function() {
                scInstance = ext.setupStatechartInstance();
                for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                id2607964_iterator < id2607964_hoist;
                id2607964_iterator++) {
                    var listener = listeners[id2607964_iterator];
                    //to
                    listener.onEntry("started");
                }
            }
            this.exitAction = function() {
                scInstance.destroy();
                ext.clearServer();
                scInstance = null;
                for (var id2609181_iterator = 0, id2609181_hoist = listeners.length;
                id2609181_iterator < id2609181_hoist;
                id2609181_iterator++) {
                    var listener = listeners[id2609181_iterator];
                    //from
                    listener.onExit("started");
                }
            }
            this.stop = function() {
                return {
                    preemptedBasicStates: {
                        initial_default: true,
                        stopped: true,
                        paused: true,
                        running: true
                    },
                    action: function() {
                        //exit states
                        var statesExited = [];
                        var lca = scxml_id2608018;
                        var nonBasicTriggerDispatcherExitBlockIteratorExpression = currentConfiguration;
                        for (var id2607964_iterator = 0, id2607964_hoist = nonBasicTriggerDispatcherExitBlockIteratorExpression.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var state = nonBasicTriggerDispatcherExitBlockIteratorExpression[id2607964_iterator];
                            if (state.ancestors.indexOf(lca) !== -1) {
                                do {
                                    statesExited.push(state);
                                } while ((state = state.parent) && state != lca && statesExited.indexOf(state) == -1)
                            }
                        }
                        //sort by depth
                        statesExited.sort(sortByDepthDeepToShallow);
                        //execute actions for each of these states
                        for (var id2607964_iterator = 0, id2607964_hoist = statesExited.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var state = statesExited[id2607964_iterator];
                            state.exitAction();
                        }
                        //transition action
                        for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var listener = listeners[id2607964_iterator];
                            //transition id
                            listener.onTransition("", "stopped", "started_stop_5");
                        }
                        //enter states
                        stopped.enterAction();
                        //update configuration
                        currentConfiguration = [
                        stopped];
                    }
                }
                return scxml_id2608018['stop']();
            }
            this.reset = function() {
                return {
                    preemptedBasicStates: {
                        initial_default: true,
                        stopped: true,
                        paused: true,
                        running: true
                    },
                    action: function() {
                        //exit states
                        var statesExited = [];
                        var lca = scxml_id2608018;
                        var nonBasicTriggerDispatcherExitBlockIteratorExpression = currentConfiguration;
                        for (var id2607964_iterator = 0, id2607964_hoist = nonBasicTriggerDispatcherExitBlockIteratorExpression.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var state = nonBasicTriggerDispatcherExitBlockIteratorExpression[id2607964_iterator];
                            if (state.ancestors.indexOf(lca) !== -1) {
                                do {
                                    statesExited.push(state);
                                } while ((state = state.parent) && state != lca && statesExited.indexOf(state) == -1)
                            }
                        }
                        //sort by depth
                        statesExited.sort(sortByDepthDeepToShallow);
                        //execute actions for each of these states
                        for (var id2607964_iterator = 0, id2607964_hoist = statesExited.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var state = statesExited[id2607964_iterator];
                            state.exitAction();
                        }
                        //transition action
                        for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var listener = listeners[id2607964_iterator];
                            //transition id
                            listener.onTransition("", "started_initial", "started_reset_6");
                        }
                        //enter states
                        started.enterAction();
                        started_initial.enterAction();
                        //update configuration
                        currentConfiguration = [
                        started_initial];
                    }
                }
                return scxml_id2608018['reset']();
            }
            this.$dispatchPrefixEvent = function(e) {
                if (e.match(stop_Regexp_id2610873)) {
                    return {
                        preemptedBasicStates: {
                            initial_default: true,
                            stopped: true,
                            paused: true,
                            running: true
                        },
                        action: function() {
                            //exit states
                            var statesExited = [];
                            var lca = scxml_id2608018;
                            var nonBasicTriggerDispatcherExitBlockIteratorExpression = currentConfiguration;
                            for (var id2607964_iterator = 0, id2607964_hoist = nonBasicTriggerDispatcherExitBlockIteratorExpression.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var state = nonBasicTriggerDispatcherExitBlockIteratorExpression[id2607964_iterator];
                                if (state.ancestors.indexOf(lca) !== -1) {
                                    do {
                                        statesExited.push(state);
                                    } while ((state = state.parent) && state != lca && statesExited.indexOf(state) == -1)
                                }
                            }
                            //sort by depth
                            statesExited.sort(sortByDepthDeepToShallow);
                            //execute actions for each of these states
                            for (var id2607964_iterator = 0, id2607964_hoist = statesExited.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var state = statesExited[id2607964_iterator];
                                state.exitAction();
                            }
                            //transition action
                            for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var listener = listeners[id2607964_iterator];
                                //transition id
                                listener.onTransition("started", "stopped", "started_stop_5");
                            }
                            //enter states
                            stopped.enterAction();
                            //update configuration
                            currentConfiguration = [
                            stopped];
                        }
                    }
                }
                if (e.match(reset_Regexp_id2610878)) {
                    return {
                        preemptedBasicStates: {
                            initial_default: true,
                            stopped: true,
                            paused: true,
                            running: true
                        },
                        action: function() {
                            //exit states
                            var statesExited = [];
                            var lca = scxml_id2608018;
                            var nonBasicTriggerDispatcherExitBlockIteratorExpression = currentConfiguration;
                            for (var id2607964_iterator = 0, id2607964_hoist = nonBasicTriggerDispatcherExitBlockIteratorExpression.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var state = nonBasicTriggerDispatcherExitBlockIteratorExpression[id2607964_iterator];
                                if (state.ancestors.indexOf(lca) !== -1) {
                                    do {
                                        statesExited.push(state);
                                    } while ((state = state.parent) && state != lca && statesExited.indexOf(state) == -1)
                                }
                            }
                            //sort by depth
                            statesExited.sort(sortByDepthDeepToShallow);
                            //execute actions for each of these states
                            for (var id2607964_iterator = 0, id2607964_hoist = statesExited.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var state = statesExited[id2607964_iterator];
                                state.exitAction();
                            }
                            //transition action
                            for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var listener = listeners[id2607964_iterator];
                                //transition id
                                listener.onTransition("started", "started_initial", "started_reset_6");
                            }
                            //enter states
                            started.enterAction();
                            started_initial.enterAction();
                            //update configuration
                            currentConfiguration = [
                            started_initial];
                        }
                    }
                }
                return scxml_id2608018.$dispatchPrefixEvent(e);
            }
        }
        startedConstructor.prototype = scxml_id2608018;
        return new startedConstructor();
    })();
    var started_initial = (function() {
        function started_initialConstructor() {
            this.parent = started;
            this.initial = null;
            this.depth = 2;
            this.historyState = null;
            //these variables facilitate fast In predicate
            this.isBasic =
            true;
            this.ancestors = [
            scxml_id2608018, started];
            this.parent.initial = this; //init parent's pointer to initial state
            this.toString = function() {
                return "started_initial"
            }
            this.enterAction = function() {
                for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                id2607964_iterator < id2607964_hoist;
                id2607964_iterator++) {
                    var listener = listeners[id2607964_iterator];
                    //to
                    listener.onEntry("started_initial");
                }
            }
            this.exitAction = function() {
                for (var id2609188_iterator = 0, id2609188_hoist = listeners.length;
                id2609188_iterator < id2609188_hoist;
                id2609188_iterator++) {
                    var listener = listeners[id2609188_iterator];
                    //from
                    listener.onExit("started_initial");
                }
            }
            this.$default = function() {
                return {
                    preemptedBasicStates: {
                        paused: true,
                        running: true
                    },
                    action: function() {
                        hasTakenDefaultTransition = true;
                        //exit states
                        started_initial.exitAction();
                        //transition action
                        for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var listener = listeners[id2607964_iterator];
                            //transition id
                            listener.onTransition("", "running", "started_initial_$default_4");
                        }
                        //enter states
                        running.enterAction();
                        //update configuration
                        currentConfiguration = [
                        running];
                    }
                }
                return started['$default']();
            }
            this.$dispatchPrefixEvent = function(e) {
                return started.$dispatchPrefixEvent(e);
            }
        }
        started_initialConstructor.prototype = started;
        return new started_initialConstructor();
    })();
    var paused = (function() {
        function pausedConstructor() {
            this.parent = started;
            this.initial = null;
            this.depth = 2;
            this.historyState = null;
            //these variables facilitate fast In predicate
            this.isBasic =
            true;
            this.ancestors = [
            scxml_id2608018, started];
            this.toString = function() {
                return "paused"
            }
            this.enterAction = function() {
                enable(ext.playButton);
                disable(ext.pauseButton);
                enable(ext.resetButton);
                enable(ext.stopButton);
                for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                id2607964_iterator < id2607964_hoist;
                id2607964_iterator++) {
                    var listener = listeners[id2607964_iterator];
                    //to
                    listener.onEntry("paused");
                }
            }
            this.exitAction = function() {
                for (var id2610332_iterator = 0, id2610332_hoist = listeners.length;
                id2610332_iterator < id2610332_hoist;
                id2610332_iterator++) {
                    var listener = listeners[id2610332_iterator];
                    //from
                    listener.onExit("paused");
                }
            }
            this.play = function() {
                return {
                    preemptedBasicStates: {
                        paused: true,
                        running: true
                    },
                    action: function() {
                        //exit states
                        paused.exitAction();
                        //transition action
                        scInstance.addListener(ext.listener)
                        scInstance.$UNPAUSE()
                        for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var listener = listeners[id2607964_iterator];
                            //transition id
                            listener.onTransition("", "running", "paused_play_7");
                        }
                        //enter states
                        running.enterAction();
                        //update configuration
                        currentConfiguration = [
                        running];
                    }
                }
                return started['play']();
            }
            this.$dispatchPrefixEvent = function(e) {
                if (e.match(play_Regexp_id2610867)) {
                    return {
                        preemptedBasicStates: {
                            paused: true,
                            running: true
                        },
                        action: function() {
                            //exit states
                            paused.exitAction();
                            //transition action
                            scInstance.addListener(ext.listener)
                            scInstance.$UNPAUSE()
                            for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var listener = listeners[id2607964_iterator];
                                //transition id
                                listener.onTransition("paused", "running", "paused_play_7");
                            }
                            //enter states
                            running.enterAction();
                            //update configuration
                            currentConfiguration = [
                            running];
                        }
                    }
                }
                return started.$dispatchPrefixEvent(e);
            }
        }
        pausedConstructor.prototype = started;
        return new pausedConstructor();
    })();
    var running = (function() {
        function runningConstructor() {
            this.parent = started;
            this.initial = null;
            this.depth = 2;
            this.historyState = null;
            //these variables facilitate fast In predicate
            this.isBasic =
            true;
            this.ancestors = [
            scxml_id2608018, started];
            this.toString = function() {
                return "running"
            }
            this.enterAction = function() {
                disable(ext.playButton);
                enable(ext.pauseButton);
                enable(ext.resetButton);
                enable(ext.stopButton);
                for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                id2607964_iterator < id2607964_hoist;
                id2607964_iterator++) {
                    var listener = listeners[id2607964_iterator];
                    //to
                    listener.onEntry("running");
                }
            }
            this.exitAction = function() {
                for (var id2610437_iterator = 0, id2610437_hoist = listeners.length;
                id2610437_iterator < id2610437_hoist;
                id2610437_iterator++) {
                    var listener = listeners[id2610437_iterator];
                    //from
                    listener.onExit("running");
                }
            }
            this.pause = function() {
                return {
                    preemptedBasicStates: {
                        paused: true,
                        running: true
                    },
                    action: function() {
                        //exit states
                        running.exitAction();
                        //transition action
                        scInstance.removeListener(ext.listener)
                        scInstance.$PAUSE()
                        for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var listener = listeners[id2607964_iterator];
                            //transition id
                            listener.onTransition("", "paused", "running_pause_8");
                        }
                        //enter states
                        paused.enterAction();
                        //update configuration
                        currentConfiguration = [
                        paused];
                    }
                }
                return started['pause']();
            }
            this.send_event = function() {
                return {
                    preemptedBasicStates: {
                        paused: true,
                        running: true
                    },
                    action: function() {
                        //exit states
                        running.exitAction();
                        //transition action
                        //send event to the scInstance
                        try {
                            scInstance[_event.data.name](_event.data.data);
                            ext.writeToConsole(scInstance.getCurrentConfiguration());
                        } catch (e) {
                            ext.writeToConsole("Error sending event: " + e.message);
                        }
                        for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                        id2607964_iterator < id2607964_hoist;
                        id2607964_iterator++) {
                            var listener = listeners[id2607964_iterator];
                            //transition id
                            listener.onTransition("", "running", "running_send_event_9");
                        }
                        //enter states
                        running.enterAction();
                        //update configuration
                        currentConfiguration = [
                        running];
                    }
                }
                return started['send_event']();
            }
            this.$dispatchPrefixEvent = function(e) {
                if (e.match(pause_Regexp_id2610884)) {
                    return {
                        preemptedBasicStates: {
                            paused: true,
                            running: true
                        },
                        action: function() {
                            //exit states
                            running.exitAction();
                            //transition action
                            scInstance.removeListener(ext.listener)
                            scInstance.$PAUSE()
                            for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var listener = listeners[id2607964_iterator];
                                //transition id
                                listener.onTransition("running", "paused", "running_pause_8");
                            }
                            //enter states
                            paused.enterAction();
                            //update configuration
                            currentConfiguration = [
                            paused];
                        }
                    }
                }
                if (e.match(send_event_Regexp_id2610890)) {
                    return {
                        preemptedBasicStates: {
                            paused: true,
                            running: true
                        },
                        action: function() {
                            //exit states
                            running.exitAction();
                            //transition action
                            //send event to the scInstance
                            try {
                                scInstance[_event.data.name](_event.data.data);
                                ext.writeToConsole(scInstance.getCurrentConfiguration());
                            } catch (e) {
                                ext.writeToConsole("Error sending event: " + e.message);
                            }
                            for (var id2607964_iterator = 0, id2607964_hoist = listeners.length;
                            id2607964_iterator < id2607964_hoist;
                            id2607964_iterator++) {
                                var listener = listeners[id2607964_iterator];
                                //transition id
                                listener.onTransition("running", "running", "running_send_event_9");
                            }
                            //enter states
                            running.enterAction();
                            //update configuration
                            currentConfiguration = [
                            running];
                        }
                    }
                }
                return started.$dispatchPrefixEvent(e);
            }
        }
        runningConstructor.prototype = started;
        return new runningConstructor();
    })();
    //states enum for glass-box unit testing
    this._states = {
        _initial: _initial,
        initial_default: initial_default,
        stopped: stopped,
        started_initial: started_initial,
        paused: paused,
        running: running
    }
    //trigger methods for synchronous interaction
    this["$default"] = function(data) {
        if (isInStableState && !destroyed) {
            runToCompletion(
            //TODO: conditionally wrap in quotes for enumerated pattern
            "$default", data, true)
        } else {
            return undefined;
        }
    }
    this["init"] = function(data) {
        if (isInStableState && !destroyed) {
            runToCompletion(
            //TODO: conditionally wrap in quotes for enumerated pattern
            "init", data, true)
        } else {
            return undefined;
        }
    }
    this["play"] = function(data) {
        if (isInStableState && !destroyed) {
            runToCompletion(
            //TODO: conditionally wrap in quotes for enumerated pattern
            "play", data, true)
        } else {
            return undefined;
        }
    }
    this["stop"] = function(data) {
        if (isInStableState && !destroyed) {
            runToCompletion(
            //TODO: conditionally wrap in quotes for enumerated pattern
            "stop", data, true)
        } else {
            return undefined;
        }
    }
    this["reset"] = function(data) {
        if (isInStableState && !destroyed) {
            runToCompletion(
            //TODO: conditionally wrap in quotes for enumerated pattern
            "reset", data, true)
        } else {
            return undefined;
        }
    }
    this["pause"] = function(data) {
        if (isInStableState && !destroyed) {
            runToCompletion(
            //TODO: conditionally wrap in quotes for enumerated pattern
            "pause", data, true)
        } else {
            return undefined;
        }
    }
    this["send_event"] = function(data) {
        if (isInStableState && !destroyed) {
            runToCompletion(
            //TODO: conditionally wrap in quotes for enumerated pattern
            "send_event", data, true)
        } else {
            return undefined;
        }
    }
    //initialization script

    function enable(e) {
        e.attr("disabled", false);
    }
    function disable(e) {
        e.attr("disabled", true);
    }
    //initialization method
    this.initialize = function() {
        currentConfiguration = [initial_default];
        runToCompletion();
        mainLoop();
    }
    //internal runtime functions

    function sortByDepthDeepToShallow(a, b) {
        return b.depth - a.depth;
    }
    //start static boilerplate code
    //static private member variables
    var currentConfiguration = []; //current configuration
    var innerEventQueue = []; //inner event queue
    var outerEventQueue = []; //outer event queue
    var isInStableState = true;
    var hasTakenDefaultTransition = false;
    var destroyed = false;
    var mainLoopCallback = null;
    //static private member functions


    function mainLoop() {
        if (!destroyed) {
            //take an event from the current outer event queue
            if (outerEventQueue.length && isInStableState) {
                runToCompletion(outerEventQueue.shift(), outerEventQueue.shift());
            }
            //call back
            mainLoopCallback = window.setTimeout(function() {
                mainLoop(); //FIXME: note that when calling mainloop this way, we won't have access to the "this" object. 
                //I don't think we ever use it though. Everything we need is private in function scope.
            }, 100);
        }
    }
    function runToCompletion(e, data, isEnumeratedEvent) {
        isInStableState = false;
        if (e) {
            innerEventQueue.push(e, data, isEnumeratedEvent);
        }
        do {
            //take any available default transitions
            microstep("$default", null, true);
            if (!hasTakenDefaultTransition) {
                if (!innerEventQueue.length) {
                    //we have no more generated events, and no default transitions fired, so
                    //we are done, and have run to completion
                    break;
                } else {
                    //microstep, then dequeue next event sending in event
                    microstep(innerEventQueue.shift(), innerEventQueue.shift(), innerEventQueue.shift());
                }
            } else {
                //he has taken a default transition, so reset the global variable to false and loop again
                hasTakenDefaultTransition = false;
            }
        } while (true)
        isInStableState = true;
    }
    function microstep(e, data, isEnumeratedEvent) {
        var enabledTransitions = [],
            transition = null,
            preemptedBasicStates = {};
        //we set the event as a global, rather than passing it into the function invocation as a parameter,
        //because in cases of default events, the event object will be populated with previous event's data
        if (e !== "$default") {
            _event.name = isEnumeratedEvent ? e : e;
            _event.data = data;
        }
        if (isEnumeratedEvent) {
            //e does not contain a dot, so dispatch as an enumerated event
            for (var id2607964_iterator = 0, id2607964_hoist = currentConfiguration.length;
            id2607964_iterator < id2607964_hoist;
            id2607964_iterator++) {
                var state = currentConfiguration[id2607964_iterator];
                //check to make sure he is not preempted
                if (!(state in preemptedBasicStates)) {
                    //lookup the transition
                    var transition = state[e]();
                    if (transition) {
                        enabledTransitions.push(transition.action);
                        mixin(transition.preemptedBasicStates, preemptedBasicStates);
                    }
                }
            }
        } else {
            //e contains a dot, so dispatch as a prefix event
            for (var id2607964_iterator = 0, id2607964_hoist = currentConfiguration.length;
            id2607964_iterator < id2607964_hoist;
            id2607964_iterator++) {
                var state = currentConfiguration[id2607964_iterator];
                //check to make sure he is not preempted
                if (!(state in preemptedBasicStates)) {
                    //lookup the transition
                    var transition = state.$dispatchPrefixEvent(e)
                    if (transition) {
                        enabledTransitions.push(transition.action);
                        mixin(transition.preemptedBasicStates, preemptedBasicStates);
                    }
                }
            }
        }
        //invoke selected transitions
        for (var id2607964_iterator = 0, id2607964_hoist = enabledTransitions.length;
        id2607964_iterator < id2607964_hoist;
        id2607964_iterator++) {
            var t = enabledTransitions[id2607964_iterator];
            t();
        }
    }
    function mixin(from, to) {
        for (var prop in from) {
            to[prop] = from[prop]
        }
    }
    this.destroy = function() {
        //right now, this only disables timer and sets global destroyed variable to prevent future callbacks
        window.clearTimeout(mainLoopCallback);
        mainLoopCallback = null;
        destroyed = true;
    }
    //this is for async communication
    this.GEN = function(e, data) {
        outerEventQueue.push(e, data);
    }
    //this may or may not be something we want to expose, but for right now, we at least need it for testing
    this.getCurrentConfiguration = function() {
        //slice it to return a copy of the configuration rather than the conf itself
        //this saves us all kinds of confusion involving references and stuff
        //TODO: refactor this name to be genCurrentConfigurationStatement 
        var currentConfigurationExpression = currentConfiguration.slice();
        return currentConfigurationExpression;
    }
    //public API for In predicate
    this.$in = function(state) {
        return In(state);
    }
    //end static boilerplate code

    function In(state) {
        state = typeof state == "string" ? self._states[state] : state;
        var toReturn;
        if (state.isBasic) {
            toReturn = currentConfiguration.indexOf(state) != -1;
        } else {
            var toReturn = false;
            for (var id2607964_iterator = 0, id2607964_hoist = currentConfiguration.length;
            id2607964_iterator < id2607964_hoist;
            id2607964_iterator++) {
                var s = currentConfiguration[id2607964_iterator];
                if (s.ancestors.indexOf(state) != -1) {
                    toReturn = true;
                    break;
                }
            }
        }
        return toReturn;
    }
    var listeners = [];
    //TODO:listeners support adding listeners for a particular state
    this.addListener = function(listener) {
        listeners.push(listener);
    }
    this.removeListener = function(listener) {
        listeners.splice(listeners.indexOf(listener), 1);
    }
}
