import Vue from "vue";
import Cookie from "js-cookie";


export const state = () => ({
    authKey: null,
    lastTime: null,
});

export const mutations = {
    setAuthKey(state, data) {

        state.authKey = data.authKey;
        state.lastTime = data.expiresIn;
    },
    clearAuthKey(state, rootState) {
        Cookie.remove("authKey");
        Cookie.remove("expiresIn");

        state.authKey = null;
        state.lastTime = null;


        //if (rootState) {
        //  rootState.Kb = null;
        //  rootState.Menu = [];
        //  rootState.MobilBilgi.dv = null;
        //  rootState.MobilBilgi.dt = null;
        //  rootState.MobilBilgi.ck = null;
        //}       
    },
    clearMobilBilgi(state, rootState) {
        if (rootState) {
            rootState.MobilBilgi.dv = null;
            rootState.MobilBilgi.dt = null;
            rootState.MobilBilgi.ck = null;

        }
    }
};

export const actions = {
    initAuth({ state, commit, rootState, dispatch }, req) {
        let token = "";
        let expiresIn;
        if (req) {
            if (!req.headers.cookie) {

                return;
            }
            token = req.headers.cookie.split(";").find(c => c.trim().startsWith("authKey="))
            if (token) {
                token = token.split("=")[1]
            }
            expiresIn = req.headers.cookie.split(";").find(e => e.trim().startsWith("expiresIn="))
            if (expiresIn) {
                expiresIn = expiresIn.split("=")[1]
            }
        } else {
            token = Cookie.get("authKey");
            //token = localStorage.getItem("authKey");
            expiresIn = Cookie.get("expiresIn");
        }
        var now = new Date().getTime();
        if (now > +expiresIn || !token) {
            commit("clearAuthKey", rootState);
        }

        commit("setAuthKey", { authKey: token, expiresIn });
        var UserData = { token: token }
        dispatch("requestUserInfo", UserData, { root: true });
    },
    authUser({ state, commit, rootState, dispatch }, authData) {
        let ths = this;
        let authLink = rootState.ApiLink + "auth/login";
        Vue.http.options.xhr = { withCredentials: true };
        Vue.http.options.emulateJSON = true;
        let data = JSON.stringify(authData);
        return Vue.http.post(authLink, data, { headers: { "Content-Type": "application/json" } })
            .then((response) => {
                let data = response.data;
                let expiresIn = new Date().getTime() + +data.expires_in * 1000;
                Cookie.set("authKey", data.access_token);
                Cookie.set("expiresIn", expiresIn);
                commit("setAuthKey", { authKey: data.access_token, expiresIn });
                var UserData = { token: data.access_token }
                dispatch("requestUserInfo", UserData, { root: true });
                if(response.status == 200){
                    ths.app.router.push("/");
                }
            });
    },
    logout({ state, commit, rootState }) {
        commit("clearAuthKey", rootState);
        let token = state.authKey;
        token = "Bearer " + token;
        let authLink = rootState.ApiLink + "auth/logout";
        return Vue.http.delete(authLink, { headers: { "Authorization": token, "Content-Type": "application/json" } })
            .then((response) => {
            });
    }

};

export const getters = {
    isAuthenticated(state) {
        return state.authKey !== null && state.authKey !== undefined && state.authKey !== "";
    },
    getToken(state) {
        return state.authKey;
    }
};
