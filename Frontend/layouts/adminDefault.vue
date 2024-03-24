<template>
    <v-app dark>
      <v-navigation-drawer
        v-model="drawer"
        :mini-variant="miniVariant"
        :clipped="clipped"
        fixed
        app
      >
        <v-list>
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :to="item.to"
            router
            exact
          >
            <v-list-item-action>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-app-bar
        :clipped-left="clipped"
        fixed
        app
      >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
        <v-toolbar-title>{{ title }}</v-toolbar-title>
        <v-spacer />
        <v-btn
          icon
          @click="returnToWebShop"
        >
          Back
        </v-btn>
      </v-app-bar>
      <v-main>
        <v-container>
          <Nuxt />
        </v-container>
      </v-main>
     
      <v-footer
        :absolute="!fixed"
        app
      >
        <span>&copy; {{ new Date().getFullYear() }}</span>
      </v-footer>
    </v-app>
  </template>
 
  <script>
import { computed } from 'vue'
  export default {
    middleware: ["session-control", "auth"],
    data () {
      return {
        clipped: false,
        drawer: false,
        fixed: false,
        miniVariant: false,
        right: true,
        rightDrawer: false,
        title: 'Admin Page'
      }
    },
    methods:{
      returnToWebShop(){
        this.$router.push("/")
      }
    },
    computed:{

      userInfo() {
                return this.$store.getters.getUserInfo;
            },
    items(){
      let list
      if(this.userInfo.role === 'manager' || this.userInfo.role === 'admin' ){
        list = [
      
          {
            icon: 'mdi-home-edit',
            title: 'Home Page Sliders',
            to: '/admin/homeSliders'
          },
          {
            icon: 'mdi-picture-in-picture-bottom-right',
            title: 'Home Page Cards',
            to: '/admin/homeCards'
          },
       
          {
            icon: 'mdi-sprout',
            title: 'Products',
            to: '/admin/productList'
          },
          {
            icon: 'mdi-account',
            title: 'Users',
            to: '/admin/users'
          },
        ]
      }else{
        list = [
          {
            icon: 'mdi-home-edit',
            title: 'Home Page Sliders',
            to: '/admin/homeSliders'
          },
          {
            icon: 'mdi-picture-in-picture-bottom-right',
            title: 'Home Page Cards',
            to: '/admin/homeCards'
          },
        ]
      }
      return list
   
     
    }
    },
    created() {
      if (process.client) {
        console.log(this.userInfo)
     this.$store.dispatch("auth/initAuth")
      }
  
    },
  }
  </script>
 

