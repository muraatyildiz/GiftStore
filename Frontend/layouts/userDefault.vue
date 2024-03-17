<template>
    <v-app id="inspire">
      <v-app-bar
        :clipped-left="$vuetify.breakpoint.lgAndUp"
        app
        color="primary"
        dark
      >
  <!--      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />-->
  
        <v-toolbar-title
          style="width: 350px"
        >
          <a href="/" class="white--text" style="text-decoration: none"><v-icon>mdi-truck</v-icon>&nbsp;ShipIT</a>
        </v-toolbar-title>
        <v-text-field
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
        <v-badge content="2" value="2" color="green" overlap>
          <v-icon>mdi-bell</v-icon>
        </v-badge>
      </v-btn>
    </nuxt-link>
    <nuxt-link to="/cart">
      <v-btn icon>
        <v-badge content="2" value="2" color="green" overlap>
          <v-icon>mdi-cart</v-icon>
        </v-badge>
      </v-btn>
    </nuxt-link>
      </v-app-bar>
      <v-content>
        <v-bottom-navigation
          :value="activeBtn"
          color="primary"
          horizontal
        >
          <a href="/" class="v-btn">
            <span>Home</span>
          </a>
          <v-menu open-on-hover offset-y>
            <template v-slot:activator="{ on }">
              <v-btn v-on="on">
                <span>Shop</span>
              </v-btn>
            </template>
            <v-card
              class="mx-auto"
              max-width="344"
              outlined
            >
  
              <v-list-item
                v-for="(item, index) in items"
                :key="index"
                href="/"
              >
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item>
  
            </v-card>
          </v-menu>
          <a href="/" class="v-btn">
            <span>Products</span>
          </a>
          <v-btn href="/">
            <span>Collections</span>
          </v-btn>
        </v-bottom-navigation>
      </v-content>
     
          <Nuxt />
    
      <v-footer
        :padless="true"
      >
        <v-card
          flat
          tile
          width="100%"
          class="secondary white--text text-center"
        >
          <v-card-text>
            <v-btn
              class="mx-4 white--text"
              icon
            >
              <v-icon size="24px">mdi-home</v-icon>
            </v-btn>
            <v-btn
              class="mx-4 white--text"
              icon
            >
              <v-icon size="24px">mdi-email</v-icon>
            </v-btn>
            <v-btn
              class="mx-4 white--text"
              icon
            >
              <v-icon size="24px">mdi-calendar</v-icon>
            </v-btn>
             <v-btn
              class="mx-4 white--text"
              icon
            >
              <v-icon size="24px">mdi-delete</v-icon>
            </v-btn>
  
          </v-card-text>
  
          <v-card-text class="white--text pt-0">
            Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum. Praesent ut risus eget metus luctus accumsan id ultrices nunc. Sed at orci sed massa consectetur dignissim a sit amet dui. Duis commodo vitae velit et faucibus. Morbi vehicula lacinia malesuada. Nulla placerat augue vel ipsum ultrices, cursus iaculis dui sollicitudin. Vestibulum eu ipsum vel diam elementum tempor vel ut orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
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
      export default {
        middleware: ["session-control", "auth"],
          data () {
              return {
                  items: [
                      { title: 'T-Shirts' },
                      { title: 'Jackets' },
                      { title: 'Shirts' },
                      { title: 'Jeans' },
                      { title: 'Shoes' },
                  ],
                  activeBtn: 1,
              }
          },
      }
  </script>