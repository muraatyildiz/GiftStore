<template>
    <div>
      <v-container>
        <p class="display-3 font-weight-light	text-center ">Wishlist</p>
          <div class="row">
            <div class="col-md-4 col-sm-4 col-xs-12">
              <v-card
                class="mx-auto"
                max-width="400"
                outlined
                tile
                href="/post"
              >
                <v-img
                  class="white--text align-end"
                  height="400px"
                  src="2.jpg"
                >
                  <v-card-title>Top 10 Fashion of the Week</v-card-title>
                </v-img>
  
                <v-card-subtitle class="pb-0">Lorem ipsum</v-card-subtitle>
  
                <v-card-text class="text--primary">
  
                  <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nibh venenatis cras sed felis eget velit aliquet sagittis id. Enim praesent elementum facilisis leo vel fringilla est ullamcorper.
  
                  </div>
                </v-card-text>
  
                <v-card-actions>
                  <v-btn
                    color="orange"
                    text
                  >
                    Read More
                  </v-btn>
                </v-card-actions>
              </v-card>
            </div>
            <div class="col-md-4 col-sm-3 col-xs-12">
              <v-card
                class="mx-auto"
                max-width="400"
                outlined
                tile
                href="/post"
              >
                <v-img
                  class="white--text align-end"
                  height="400px"
                  src="3.jpg"
                >
                  <v-card-title>Best brands for fashion</v-card-title>
                </v-img>
  
                <v-card-subtitle class="pb-0">Lorem ipsum</v-card-subtitle>
  
                <v-card-text class="text--primary">
  
                  <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nibh venenatis cras sed felis eget velit aliquet sagittis id. Enim praesent elementum facilisis leo vel fringilla est ullamcorper.
  
                  </div>
                </v-card-text>
  
                <v-card-actions>
                  <v-btn
                    color="orange"
                    text
                  >
                    Read More
                  </v-btn>
                </v-card-actions>
              </v-card>
            </div>
            <div class="col-md-4 col-sm-3 col-xs-12">
            <v-hover v-slot:default="{ hover }">
              <v-card
                class="mx-auto"
                max-width="400"
                outlined
                tile
                href="/post"
              >
                <v-img
                  class="white--text align-end"
                  height="400px"
                  src="4.jpg"
                >
                  <v-card-title>Fashion Tips & Tricks</v-card-title>
                  <v-expand-transition>
                      <div
                        v-if="hover"
                        class="d-flex transition-fast-in-fast-out white darken-2 v-card--reveal display-3 white--text"
                        style="height: 100%"
                      >
                      <v-btn v-if="hover" href="/product" class="" outlined
                          >Remove</v-btn
                        >
                        <v-btn v-if="hover" href="/product" class="" outlined
                          >Add Cart</v-btn
                        >
                      </div>
                    </v-expand-transition>
                </v-img>
          
                <v-card-subtitle class="pb-0">Lorem ipsum</v-card-subtitle>
  
                <v-card-text class="text--primary">
  
                  <div>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nibh venenatis cras sed felis eget velit aliquet sagittis id. Enim praesent elementum facilisis leo vel fringilla est ullamcorper.
  
                  </div>
                </v-card-text>
  
                <v-card-actions>
                  <v-btn
                    color="orange"
                    text
                  >
                    Read More
                  </v-btn>
                </v-card-actions>
              </v-card>
           
            </v-hover>
                    </div>
          </div>
      </v-container>
    </div>
  </template>
  <script>
export default {
  layout: "userDefault",
};
</script>
  