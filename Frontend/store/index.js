import Vue from "vue";

export const state = () => ({
	ApiLink: process.env.NODE_ENV === "development" ? "http://172.20.10.8:8080/" : "/",
	ApiLink2: process.env.NODE_ENV === "development" ? "http://172.20.10.8:8080/" : "/",
	userInfo :null,
});

export const mutations = {
	setUserInfo(state, user) {
		if (user) {
			state.userInfo = user;
		}
		else {
			state.userInfo = null;
		}
	}
};

export const actions = {
	requestPost(vuexContext, send) {
		let token = vuexContext.getters["auth/getToken"];
		token = "Bearer " + token;
		send.link = vuexContext.state.ApiLink + send.link;
		return Vue.http.post(send.link, send.data, { headers: { "Authorization": token } }).catch((r) => {
			if (r && r.status && r.status === 401) {
				vuexContext.dispatch("auth/logout");
				if (process.client) {
					this.app.router.push("/login");
				}
			} else { console.log("Error", r); }
		});
	},
	requestGet(vuexContext, link) {
		let token = vuexContext.getters["auth/getToken"];
		token = "Bearer " + token;
		link = vuexContext.state.ApiLink + link;
		return Vue.http.get(link, { headers: { "Authorization": token } }).catch((r) => {
			if (r && r.status && r.status === 401) {
				vuexContext.dispatch("auth/logout");
				if (process.client) {
					this.app.router.push("/login");
				}
			} else { console.log("Error", r); }
			});
	},
	requestUserInfo({ state, commit, rootState, dispatch }, commingToken) {
		let ths = this;
		let token = commingToken.token;
		token = "Bearer " + token;
		var link = rootState.ApiLink + "userInfo";
			Vue.http.get(link, { headers: { "Authorization": token } }).then((response) => {
			var answer = response.body;
			if (answer.Durum) {
				commit("setUserInfo", answer.Veri);			
				ths.app.router.push("/");
			}
		}).catch((r) => {			
			console.log("User info", r);
		});


	}
};

export const getters = {
	getUserInfo(state) {
		if (state.userInfo) {
			return state.userInfo;
		}
		return null;
	}
};