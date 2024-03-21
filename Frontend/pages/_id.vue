<template>
    <div>
      <v-container>
        <div class="row">
          <div class="col-md-5 col-sm-5 col-xs-12">
            <v-carousel>
              <v-carousel-item
              :src="
                      $store.state.ApiLink + 'file/serve-image/' + product.imgUrl
                    "
              >
              </v-carousel-item>
              <!-- <v-carousel-item
                src="require('../assets/img/home/slider2.jpg')"
              >
              </v-carousel-item>
              <v-carousel-item
                src="require('../assets/img/home/slider3.jpg')"
              >
              </v-carousel-item>
              <v-carousel-item
                src="require('../assets/img/home/slider1.jpg')"
              >
              </v-carousel-item> -->
  
            </v-carousel>
          </div>
          <div class="col-md-7 col-sm-7 col-xs-12">
            <v-breadcrumbs class="pb-0" :items="breadcrums"></v-breadcrumbs>
            <div class="pl-6">
              <p class="display-1 mb-0">{{ product.name }}</p>
              <v-card-actions class="pa-0">
                <p class="headline font-weight-light pt-3">€{{ product.price }} <del style="" class="subtitle-1 font-weight-thin">€{{ product.price + 20 }}</del></p>
                <v-spacer></v-spacer>
                <v-rating v-model="rating" class="" background-color="warning lighten-3"
                          color="warning" dense></v-rating>
                <span class="body-2	font-weight-thin"> 25 REVIEWS</span>
              </v-card-actions>
              <p class="subtitle-1 font-weight-thin">
               {{ product.description }}
              </p>
              <p class="title">ITEMS</p>
  
              <v-text-field
                  outlined
                  style="width:100px"
                  :value="1"
                  dense
              ></v-text-field>
              <v-btn class="primary white--text" outlined tile dense><v-icon>mdi-cart</v-icon> ADD TO CART</v-btn>
              <v-btn class="ml-4" outlined tile>ADD TO WISHLIST</v-btn>
  
            </div>
  
          </di>
        </div>
        </div>
        <div class="row">
          <div class="col-sm-12 col-xs-12 col-md-12">
            <v-tabs>
              <v-tab >Description</v-tab>
              <v-tab >Materials</v-tab>
             
              <v-tab-item>
                <p class="pt-10 subtitle-1 font-weight-thin">
                 {{ product.description }}
                </p>
              </v-tab-item>
              <v-tab-item>
                <p class="pt-10 subtitle-1 font-weight-thin">
                    {{ product.description }}
                </p>
              </v-tab-item>
            </v-tabs>
            <v-card-text
              class="pa-0 pt-4"
              tile
              outlined
            >
              <p class="subtitle-1 font-weight-light pt-3 text-center">YOU MIGHT ALSO LIKE</p>
              <v-divider></v-divider>
              <div class="row text-center">
                <div class="col-md-2 col-sm-4 col-xs-12 text-center"  :key="product.id"
              v-for="product in products">
                  <v-hover
                    v-slot:default="{ hover }"
                    open-delay="200"
                  >
                    <v-card
                      :elevation="hover ? 16 : 2"
                    >
                      <v-img
                        class="white--text align-end"
                        height="200px"
                        :src="
                      $store.state.ApiLink + 'file/serve-image/' + product.imgUrl
                    "
                      >
                        <v-card-title>{{product.name}} </v-card-title>
                      </v-img>
  
                      <v-card-text class="text--primary text-center">
                        <div>Upto 60% + Extra 10%</div>
                        <!-- <div>{{product.name}}</div> -->
                      </v-card-text>
  
                      <div class="text-center">
                        <v-btn
                         :href="`/${product._id}`"
                          class="ma-2"
                          outlined
                          color="info"
                        >
                          Explore
                        </v-btn>
                      </div>
                    </v-card>
                  </v-hover>
                </div>
              </div>
            </v-card-text>
          </div>
        </div>
      </v-container>
      <v-card  class="accent" >
        <v-container>
          <v-row no-gutters>
            <v-col class="col-12 col-md-4 col-sm-12">
              <v-row >
                <v-col class="col-12 col-sm-3 pr-4 hidden-sm-only" align="right">
                  <v-icon class="display-2">mdi-truck</v-icon>
                </v-col>
                <v-col class="col-12 col-sm-9 pr-4">
                  <h3 class="font-weight-light">FREE SHIPPING & RETURN</h3>
                  <p class="font-weight-thin">Free Shipping over €300</p>
                </v-col>
              </v-row>
            </v-col>
            <v-col class="col-12 col-md-4 col-sm-12">
              <v-row >
                <v-col class="col-12 col-sm-3 pr-4" align="right">
                  <v-icon class="display-2">mdi-cash-usd</v-icon>
                </v-col>
                <v-col  class="col-12 col-sm-9 pr-4">
                  <h3 class="font-weight-light">MONEY BACK GUARANTEE</h3>
                  <p class="font-weight-thin">30 Days Money Back Guarantee</p>
                </v-col>
              </v-row>
            </v-col>
            <v-col class="col-12 col-md-4 col-sm-12">
              <v-row>
                <v-col class="col-12 col-sm-3 pr-4" align="right">
                  <v-icon class="display-2">mdi-headset</v-icon>
                </v-col>
                <v-col  class="col-12 col-sm-9 pr-4">
                  <h3 class="font-weight-light">020-800-456-747</h3>
                  <p class="font-weight-thin">24/7 Available Support</p>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </div>
  </template>
  <script>
export default {
  data: () => ({
    rating: 3,
    product: {},
    products:[],
    breadcrums: [
      {
        text: "Home",
        disabled: false,
        href: "/",
      },
      {
        text: "Clothing",
        disabled: false,
        href: "/",
      },
      {
        text:'',
        disabled: true,
        href: "/",
      },
    ],
    item: 5,
  }),
  methods: {
    getProduct() {
      let id = this.$route.params.id;
      let link = "product/"+ id;
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          if (response.status == 200) {
            this.product = response.data.product;
            this.breadcrums[2].text = this.product.category;
            this.breadcrums[2].text= this.breadcrums[2].text.charAt(0).toUpperCase() + this.breadcrums[2].text.slice(1);
          }
        })
        .catch((x) => {
          console.log("Error");
        });
       
    },
    getProductlist(){
        let productIdToRemove = this.$route.params.id;
        let link = `product/list`;
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          if (response.status == 200) {
            this.products = response.data.products;
            this.products = this.products.filter(product => product._id !== productIdToRemove);
            this.products = this.products.slice(0, 6);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
  },
  created() {
    if (process.client) {
      this.getProduct();
      this.getProductlist();
    }
  },
};
</script>