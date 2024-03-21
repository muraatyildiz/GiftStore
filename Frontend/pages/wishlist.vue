<template>
  <div>
    <v-container>
      <p class="display-3 font-weight-light text-center">Wishlist</p>
      <div class="row">
        <div
          v-for="(product, index) in getProductsInWishlist"
          :key="index"
          class="col-md-4 col-sm-3 col-xs-12"
        >
          <v-hover v-slot:default="{ hover }">
            <v-card class="mx-auto" max-width="400" outlined tile >
              <v-img
                class="white--text align-end"
                height="400px"
                :src="
                  $store.state.ApiLink + 'file/serve-image/' + product.imgUrl
                "
              >
                <v-card-title>{{ product.name }}</v-card-title>
                <v-expand-transition>
                  <div
                    v-if="hover"
                    class="d-flex transition-fast-in-fast-out white darken-2 v-card--reveal display-3 white--text"
                    style="height: 100%"
                  >
                    <v-btn v-if="hover" class="" outlined @click="removeProduct(product)"
                      >Remove</v-btn
                    >
                    <v-btn v-if="hover" class="" outlined  @click="addToCart(product)"
                      >Add Cart</v-btn
                    >
                  </div>
                </v-expand-transition>
              </v-img>

              <v-card-subtitle class="pb-0">{{ product.name }}</v-card-subtitle>

              <v-card-text class="text--primary">
                <div>
              {{ product.desription }}
                </div>
              </v-card-text>

              <v-card-actions>
                <v-btn color="orange" :to="`/${product._id}`" text> Product Details </v-btn>
              </v-card-actions>
            </v-card>
          </v-hover>
        </div>
      </div>
    </v-container>
  </div>
</template>
  <script>
import { mapGetters, mapMutations } from "vuex";
export default {
  layout: "userDefault",
  data: () => ({}),
  methods: {
    ...mapMutations(["removeProductFromWishlist","addProductToCart"]),
    removeProduct(product) {
      let index = this.getProductsInWishlist.indexOf(product);
      this.removeProductFromWishlist(index);
    },
    addToCart(product) {
       this.addProductToCart(product);
       this.removeProduct(product);
    },
  },

  computed: {
    ...mapGetters(["getProductsInWishlist"]),
  },
};
</script>
  