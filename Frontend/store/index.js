import Vue from "vue";

export const state = () => ({
	ApiLink: process.env.NODE_ENV === "development" ? "http://127.0.0.1:5000/" : "/",
	ApiLink2: process.env.NODE_ENV === "development" ? "http://20.218.157.149:8080/" : "/",
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
		return Vue.http.post(send.link, send.data, { headers: { "Authorization": token ,"Content-Type": "application/json"} }).catch((r) => {
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
		return Vue.http.get(link, { headers: { "Authorization": token ,"Content-Type": "application/json" } }).catch((r) => {
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
		var link = rootState.ApiLink + "auth/userInfo";
			Vue.http.get(link, { headers: { "Authorization": token,"Content-Type": "application/json"  } }).then((response) => {
			var answer = response.body;
			console.log('answer',response)
			if (response.status == 200) {
				commit("setUserInfo", answer.user);			
				ths.app.router.push("/");
			}
		}).catch((r) => {			
			console.log("User info", r);
		});
	},
	requestPut(vuexContext, send) {
		let token = vuexContext.getters["auth/getToken"];
		token = "Bearer " + token;
		send.link = vuexContext.state.ApiLink + send.link;
		return Vue.http.put(send.link, send.data, { headers: { "Authorization": token,"Content-Type": "application/json"  } }).catch((r) => {
			if (r && r.status && r.status === 401) {
				vuexContext.dispatch("auth/logout");
				
			} else { console.log("Error", r); }
			});
	},
	requestDelete(vuexContext, link) {
		let token = vuexContext.getters["auth/getToken"];
		token = "Bearer " + token;
		link = vuexContext.state.ApiLink + link;
		return Vue.http.delete(link, { headers: { "Authorization": token ,"Content-Type": "application/json" }, }).catch((r) => {
			if (r && r.status && r.status === 401) {
				vuexContext.dispatch("auth/logout");
				
			} else { console.log("Error", r); }
			});
	},

};

export const getters = {
	getUserInfo(state) {
		console.log(state)
			return state.userInfo;
		
	}
};