<template>
  <v-app id="inspire">
    <v-app-bar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      app
      color="primary"
      dark
    >
      <!--      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />-->

      <v-toolbar-title style="width: 350px">
        <nuxt-link to="/" class="white--text" style="text-decoration: none"
          ><img
            src="logo.png"
            alt="ShipIT Logo"
            style="vertical-align: middle; height: 50px; margin-right: 8px"
        /></nuxt-link>
      </v-toolbar-title>
      <v-text-field
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-magnify"
        label="Search"
        v-model="search"
        class="hidden-sm-and-down pl-10 ml-4"
      />
      <v-spacer />
      <nuxt-link to="/user">
        <v-btn icon>
          <v-icon>mdi-account-circle</v-icon>
        </v-btn>
      </nuxt-link>
      <nuxt-link to="/wishlist">
        <v-btn icon>
          <v-badge
            v-if="getProductsInWishlist.length > 0"
            :content="getProductsInWishlist.length"
            value="2"
            color="green"
            overlap
          >
            <v-icon>mdi-bell</v-icon>
          </v-badge>
          <v-icon v-else>mdi-bell</v-icon>
        </v-btn>
      </nuxt-link>
      <nuxt-link to="/cart">
        <v-btn icon>
          <v-badge
            v-if="getProductsInCart.length > 0"
            :content="getProductsInCart.length"
            value="2"
            color="green"
            overlap
          >
            <v-icon>mdi-cart</v-icon>
          </v-badge>

          <v-icon v-else>mdi-cart</v-icon>
        </v-btn>
      </nuxt-link>
    </v-app-bar>
    <v-content>
      <v-bottom-navigation :value="activeBtn" color="primary" horizontal>
        <nuxt-link to="/" class="v-btn">
          <span>Home</span>
        </nuxt-link>
        <nuxt-link to="/shop" class="v-btn">
          <span>Shop</span>
        </nuxt-link>

        <nuxt-link to="/shop" class="v-btn">
          <span>Products</span>
        </nuxt-link>

        <nuxt-link to="/shop" class="v-btn">
          <span>Collections</span>
        </nuxt-link>
      </v-bottom-navigation>
    </v-content>

    <Nuxt />

    <v-footer :padless="true">
      <v-card flat tile width="100%" class="secondary white--text text-center">
        <v-card-text>
          <v-btn to="/" class="mx-4 white--text" icon>
            <v-icon size="24px">mdi-home</v-icon>
          </v-btn>
          <v-btn to="/shop" class="mx-4 white--text" icon>
            <v-icon size="24px">mdi-email</v-icon>
          </v-btn>
          <v-btn to="/shop" class="mx-4 white--text" icon>
            <v-icon size="24px">mdi-calendar</v-icon>
          </v-btn>
          <v-btn to="/shop" class="mx-4 white--text" icon>
            <v-icon size="24px">mdi-delete</v-icon>
          </v-btn>
        </v-card-text>

        <v-card-text class="white--text pt-0">
          Our gift web shop offers a diverse array of thoughtful presents to
          suit every occasion. With a curated selection ranging from elegant to
          quirky, we aim to delight recipients and make gifting a joyous
          experience. Browse through our collection of unique items, carefully
          chosen to spark joy and create lasting memories. Whether you're
          celebrating a special milestone or simply expressing appreciation, our
          range of products ensures there's something for everyone. Experience
          the convenience of shopping online with us, where quality meets
          convenience. Discover the perfect gift today and let us help you make
          every moment unforgettable.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>Gift Shop</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>
<script>
import { mapGetters, mapActions } from "vuex";
export default {
  data() {
    return {
      items: [
        { title: "T-Shirts" },
        { title: "Jackets" },
        { title: "Shirts" },
        { title: "Jeans" },
        { title: "Shoes" },
      ],
      activeBtn: 1,
      search: "",
    };
  },
  watch: {
    search() {
      if (this.$route.name !== "shop") {
        if (this.search) {
          this.$router.push({ name: "shop", query: { search: this.search } });
        } else {
          // Handle the case where search is empty
          this.$router.push({ name: "shop" }); // Navigate to the "shop" page without query
        }
      } else if (this.search !== this.$route.query.search) {
        // If already on the "shop" page but the search query has changed
        this.$router.replace({ query: { search: this.search } });
      }
    },
  },
  computed: {
    ...mapGetters(["getProductsInCart", "getProductsInWishlist"]),
  },
};
</script>