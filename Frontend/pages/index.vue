<template>
  <div>
    <v-carousel hide-delimiters>
      <v-carousel-item v-for="(slider, index) in sliders" :key="index"  :src="$store.state.ApiLink + 'file/serve-image/' + slider.imgUrl">
        <nuxt-link  style="text-decoration: none; color: inherit;" :to="`${slider.route}`">
        <v-row class="fill-height" align="center" justify="center">
          <div class="display-2 white--text pl-5 pr-5 hidden-sm-only">
            <strong>{{slider.header}}</strong>
          </div>
          <br />
        </v-row>
      </nuxt-link>
      </v-carousel-item>
    </v-carousel>
    <div class="pl-4 pr-4 row mt-2">
      <div v-for="(card,index) in cards.slice(0, 2)" :key="index" class="col-md-6 col-sm-6 col-xs-12">
        <v-card>
          <v-img
          :src="$store.state.ApiLink + 'file/serve-image/' + card.imgUrl"
            class="white--text align-center"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="400px"
            :alt="card.altText"
          >
            <h1 class="text-center font-size">{{ card.header }}</h1>
            <div class="text-center">
              <v-btn to="/shop" class="white--text" outlined>SHOP NOW</v-btn>
            </div>

          </v-img>
        </v-card>
     
      </div>
     
    </div>
    <div class="pl-4 pr-4 row">
      <div v-for="(card,index) in cards.slice(-3)" :key="index" class="col-md-4 col-sm-4 col-xs-12">
        <v-card outlined>
          <v-img
           :src="$store.state.ApiLink + 'file/serve-image/' + card.imgUrl"
            class="white--text align-center"
            gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
            height="300px"
            :alt="card.altText"
          >
            <h1 class="text-center font-size">{{card.header}}</h1>
            <div class="text-center mt-2">
              <v-btn class="white--text caption" to="/shop" text
                >SHOP NOW
                <v-icon class="white--text caption"
                  >mdi-arrow-right</v-icon
                ></v-btn
              >
            </div>
          </v-img>
        </v-card>
      </div>
    
    </div>
    <v-container>
      <v-row no-gutters>
        <v-col :cols="12">
          <v-card-text class="" tile outlined>
            <v-card-title class="subheading">Deals of the Day</v-card-title>
            <v-divider></v-divider>
            <div class="row">
              <div v-for="(product, index) in products" :key="index" class="col-12 col-md-3 col-sm-6 col-xs-6 text-center">
                <v-hover v-slot:default="{ hover }" open-delay="200">
                  <v-card :elevation="hover ? 16 : 2">
                    <v-img
                      class="white--text align-end"
                      height="200px"
                      :src="
                      $store.state.ApiLink + 'file/serve-image/' + product.imgUrl
                    "
                    >
                      <v-card-title>{{product.name}}</v-card-title>
                    </v-img>

                    <v-card-text class="text--primary text-center">
                      <div>Upto 60% + Extra 10%</div>
                    </v-card-text>

                    <div class="text-center">
                      <v-btn  :to="`/${product._id}`" class="ma-2" outlined color="info">
                        Explore
                      </v-btn>
                    </div>
                  </v-card>
                </v-hover>
              </div>
          
            </div>
          </v-card-text>
        </v-col>
      </v-row>
    </v-container>
    <v-card class="accent">
      <v-container>
        <v-row no-gutters>
          <v-col class="col-12 col-md-4 col-sm-12">
            <v-row>
              <v-col class="col-12 col-sm-3 pr-4" align="right">
                <v-icon class="display-2">mdi-truck</v-icon>
              </v-col>
              <v-col class="col-12 col-sm-9 pr-4">
                <h3 class="font-weight-light">FREE SHIPPING & RETURN</h3>
                <p class="font-weight-thin">Free Shipping over €300</p>
              </v-col>
            </v-row>
          </v-col>
          <v-col class="col-12 col-md-4 col-sm-12">
            <v-row>
              <v-col class="col-12 col-sm-3 pr-4" align="right">
                <v-icon class="display-2">mdi-cash-usd</v-icon>
              </v-col>
              <v-col class="col-12 col-sm-9 pr-4">
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
              <v-col class="col-12 col-sm-9 pr-4">
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
  data() {
    return {
      items: [
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me" },
        { title: "Click Me 2" },
      ],
      activeBtn: 1,
      colors: [
        "indigo",
        "warning",
        "pink darken-2",
        "red lighten-1",
        "deep-purple accent-4",
      ],
      slides: ["First", "Second", "Third", "Fourth", "Fifth"],
      products:[],
      sliders:[],
      cards:[],
    };
  },
  methods:{
    getProductlist(){
        let productIdToRemove = this.$route.params.id;
        let link = `product/list`;
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          if (response.status == 200) {
            this.products = response.data.products;
            this.products = this.products.slice(0, 4);
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    getCardList() {
        let link = "homepage/cardList";
        this.$store
          .dispatch("requestGet", link)
          .then((response) => {
            var answer = response.body;
            if (response.status == 200) {
              this.cards = answer;
            }
          })
          .catch((x) => {
            console.log("Error");
          });
      },
    getSliderList() {
      let link = "homepage/sliderList";
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          var answer = response.body;
          if (response.status == 200) {
            this.sliders = answer;
          }
        })
        .catch((x) => {
          console.log("Error");
        });
    },

  },

  created() {
    if (process.client) {
      this.getProductlist();
      this.getSliderList();
      this.getCardList();
    }
  },
};
</script>
<style>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.5;
  position: absolute;
  width: 100%;
}
</style>
