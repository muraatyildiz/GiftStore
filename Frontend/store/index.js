import Vue from "vue";

export const state = () => ({
    ApiLink: process.env.NODE_ENV === "development" ? "http://127.0.0.1:8080/" : "https://gift-shop-backend-8g7v.onrender.com/",
    userInfo: null,
    cartProducts: [],
    wishlistProducts: []
});

export const mutations = {
    setUserInfo(state, user) {
        if (user) {
            state.userInfo = user;
        }
        else {
            state.userInfo = null;
        }
    },
    addProductToCart(state, product) {
        if (state.cartProducts.includes(product)) {
            product.quantity = state.cartProducts[state.cartProducts.indexOf(product)].quantity + 1
            state.cartProducts[state.cartProducts.indexOf(product)] = product
        } else {
            product.quantity = 1
            state.cartProducts.push(product);
        }
    },
    removeProductFromCart(state, index) {
        state.cartProducts.splice(index, 1)
    },
    addProductToWishlist(state, product) {
        if (state.wishlistProducts.includes(product)) {
            product.quantity = state.wishlistProducts[state.wishlistProducts.indexOf(product)].quantity + 1
            state.wishlistProducts[state.wishlistProducts.indexOf(product)] = product
        } else {
            product.quantity = 1
            state.wishlistProducts.push(product);
        }
    },
    removeProductFromWishlist(state, index) {
        state.wishlistProducts.splice(index, 1)
    }
};

export const actions = {
    requestPost(vuexContext, send) {
        let token = vuexContext.getters["auth/getToken"];
        token = "Bearer " + token;
        send.link = vuexContext.state.ApiLink + send.link;
        return Vue.http.post(send.link, send.data, { headers: { "Authorization": token, "Content-Type": "application/json" } }).catch((r) => {
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
        return Vue.http.get(link, { headers: { "Authorization": token, "Content-Type": "application/json" } }).catch((r) => {
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
        Vue.http.get(link, { headers: { "Authorization": token, "Content-Type": "application/json" } }).then((response) => {
            var answer = response.body;
            if (response.status == 200) {
                commit("setUserInfo", answer.user);
            }
        }).catch((r) => {
            console.log("User info", r);
        });
    },
    requestPut(vuexContext, send) {
        let token = vuexContext.getters["auth/getToken"];
        token = "Bearer " + token;
        send.link = vuexContext.state.ApiLink + send.link;
        return Vue.http.put(send.link, send.data, { headers: { "Authorization": token, "Content-Type": "application/json" } }).catch((r) => {
            if (r && r.status && r.status === 401) {
                vuexContext.dispatch("auth/logout");

            } else { console.log("Error", r); }
        });
    },
    requestDelete(vuexContext, link) {
        let token = vuexContext.getters["auth/getToken"];
        token = "Bearer " + token;
        link = vuexContext.state.ApiLink + link;
        return Vue.http.delete(link, { headers: { "Authorization": token, "Content-Type": "application/json" }, }).catch((r) => {
            if (r && r.status && r.status === 401) {
                vuexContext.dispatch("auth/logout");

            } else { console.log("Error", r); }
        });
    },

};

export const getters = {
    getUserInfo(state) {
        return state.userInfo;

    },

    getProductsInCart(state) {
        return state.cartProducts;
    }, getProductsInWishlist(state) {
        return state.wishlistProducts;
    }
};
