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
          ><v-icon>mdi-truck</v-icon>&nbsp;ShipIT</nuxt-link
        >
      </v-toolbar-title>
      <v-text-field
      v-model="search"
        flat
        solo-inverted
        hide-details
        prepend-inner-icon="mdi-magnify"
        label="Search"
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
          <v-btn class="mx-4 white--text" icon to="/">
            <v-icon size="24px">mdi-home</v-icon>
          </v-btn>
          <v-btn class="mx-4 white--text" icon to="/shop">
            <v-icon size="24px">mdi-email</v-icon>
          </v-btn>
          <v-btn class="mx-4 white--text" icon to="/shop">
            <v-icon size="24px">mdi-calendar</v-icon>
          </v-btn>
          <v-btn class="mx-4 white--text" icon to="/shop">
            <v-icon size="24px">mdi-delete</v-icon>
          </v-btn>
        </v-card-text>

        <v-card-text class="white--text pt-0">
          Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet.
          Mauris cursus commodo interdum. Praesent ut risus eget metus luctus
          accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim
          a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula
          lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus
          iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum
          tempor vel ut orci. Orci varius natoque penatibus et magnis dis
          parturient montes, nascetur ridiculus mus.
        </v-card-text>

        <v-divider></v-divider>

        <v-card-text class="white--text">
          {{ new Date().getFullYear() }} — <strong>ShipIT</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>
  <script>
import { mapGetters, mapActions } from "vuex";
export default {
  middleware: ["session-control", "auth"],
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
      if (this.$route.name !== 'shop') {
      if (this.search) {
        this.$router.push({ name: 'shop', query: { search: this.search } });
      } else {
        // Handle the case where search is empty
        this.$router.push({ name: 'shop' }); // Navigate to the "shop" page without query
      }
    } else if (this.search !== this.$route.query.search) {
      // If already on the "shop" page but the search query has changed
      this.$router.replace({ query: { search: this.search } });
    }
  }
  },
  computed: {
    ...mapGetters(["getProductsInCart", "getProductsInWishlist"]),
  },
};
</script>