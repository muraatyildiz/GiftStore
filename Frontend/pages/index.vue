<template>
  <div>
    <v-container>
      <div class="row">
        <div class="col-md-3 col-sm-3 col-xs-12">
          <v-card outlined>
            <v-card-title>Filters</v-card-title>
            <v-divider></v-divider>
            <template>
              <v-treeview
                :items="items"
                :selected-color="'#fff'"
                activatable
                @update:active="selectCategory"
                open-on-click
                dense
              ></v-treeview>
            </template>
            <v-divider></v-divider>
            <v-card-title>Price</v-card-title>
            <v-range-slider
              v-model="range"
              :max="max"
              :min="min"
              :height="10"
              class="align-center"
              dense
            ></v-range-slider>
            <v-row class="pa-2" dense>
              <v-col cols="12" sm="5">
                <v-text-field
                  :value="range[0]"
                  label="Min"
                  outlined
                  dense
                  @change="$set(range, 0, $event)"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2">
                <p class="pt-2 text-center">TO</p>
              </v-col>
              <v-col cols="12" sm="5">
                <v-text-field
                  :value="range[1]"
                  label="Max"
                  outlined
                  dense
                  @change="$set(range, 1, $event)"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title class="pb-0">Customer Rating</v-card-title>
            <v-container class="pt-0" fluid>
              <v-checkbox
                append-icon="mdi-star"
                label="4 & above"
                hide-details
                dense
              ></v-checkbox>
              <v-checkbox
                append-icon="mdi-star"
                label="3 & above"
                hide-details
                dense
              ></v-checkbox>
              <v-checkbox
                append-icon="mdi-star"
                label="2 & above"
                hide-details
                dense
              ></v-checkbox>
              <v-checkbox
                append-icon="mdi-star"
                label="1 & above"
                hide-details
                dense
              ></v-checkbox>
            </v-container>
            <v-divider></v-divider>
            <v-card-title class="pb-0">Brand</v-card-title>
            <v-container class="pt-0" fluid>
              <v-checkbox label="XS" hide-details dense></v-checkbox>
              <v-checkbox label="S" hide-details dense></v-checkbox>
              <v-checkbox label="M" hide-details dense></v-checkbox>
              <v-checkbox label="L" hide-details dense></v-checkbox>
              <v-checkbox label="XL" hide-details dense></v-checkbox>
              <v-checkbox label="XXL" hide-details dense></v-checkbox>
              <v-checkbox label="XXXL" hide-details dense></v-checkbox>
            </v-container>
          </v-card>
        </div>
        <div class="col-md-9 col-sm-9 col-xs-12">
          <v-breadcrumbs class="pb-0" :items="breadcrums"></v-breadcrumbs>

          <v-row dense>
            <v-col cols="12" sm="8" class="pl-6 pt-6">
              <small
                >Showing {{ (page - 1) * 12 + 1 }}-{{
                  page == pages ? totalPoruducts : page * 12
                }}
                of {{ totalPoruducts }} products</small
              >
            </v-col>
            <v-col cols="12" sm="4">
              <v-select
                class="pa-0"
                v-model="select"
                :items="options"
                style="margin-bottom: -20px"
                outlined
                dense
              ></v-select>
            </v-col>
          </v-row>

          <v-divider></v-divider>

          <div class="row text-center">
            <div
              class="col-md-3 col-sm-6 col-xs-12"
              :key="pro.id"
              v-for="pro in products"
            >
              <v-hover v-slot:default="{ hover }">
                <v-card class="mx-auto" color="grey lighten-4" max-width="600">
                  <v-img
                    class="white--text align-end"
                    :aspect-ratio="16 / 9"
                    height="200px"
                    :src="
                      $store.state.ApiLink + 'file/serve-image/' + pro.imgUrl
                    "
                  >
                    <v-card-title>{{ pro.category }} </v-card-title>
                    <v-expand-transition>
                      <div
                        v-if="hover"
                        class="d-flex transition-fast-in-fast-out white darken-2 v-card--reveal display-3 white--text"
                        style="height: 100%"
                      >
                        <v-btn v-if="hover" href="/product" class="" outlined
                          >VIEW</v-btn
                        >
                      </div>
                    </v-expand-transition>
                  </v-img>
                  <v-card-text class="text--primary">
                    <div>
                      <a href="/product" style="text-decoration: none">{{
                        pro.name
                      }}</a>
                    </div>
                    <div>${{ pro.price }}</div>
                  </v-card-text>
                </v-card>
              </v-hover>
            </div>
          </div>
          <div class="text-center mt-12">
            <v-pagination
              v-model="page"
              @input="next"
              :length="pages"
            ></v-pagination>
          </div>
        </div>
      </div>
    </v-container>
  </div>
</template>
<style>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.8;
  position: absolute;
  width: 100%;
}
</style>
<script>
export default {
  data: () => ({
    range: [0, 10000],
    select: "Popularity",
    options: [
      "Default",
      "Popularity",
      "Relevance",
      "Price: Low to High",
      "Price: High to Low",
    ],
    page: 1,
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
        text: "T-Shirts",
        disabled: true,
        href: "/",
      },
    ],
    min: 0,
    max: 10000,
    items: [
      {
        id: 2,
        name: "Shoes",
        children: [
          { id: 2, name: "event" },
          { id: 3, name: "flowers" },
          { id: 4, name: "christmas" },
        ],
      },
      {
        id: 1,
        name: "Clothing",
        children: [
          { id: 5, name: "event" },
          { id: 6, name: "flowers" },
          { id: 7, name: "christmas" },
        ],
      },
    ],
    products: [],
    filteredProducts:[],
    pages: null,
    totalPoruducts: null,
    search: "",
  }),
  watch: {
    "$route.query"() {
      if (this.$route.query.search && this.$route.query.search.length > 2) {
        this.getProductList(1, this.$route.query.search);
      } else {
        this.getProductList(1, this.search);
      }
    },
  },
  methods: {
    selectCategory(selectedItems) {
      let selectCategory;
      const selectedItem = selectedItems[selectedItems.length - 1];
      for (const item of this.items) {
        const foundChild = item.children.find(
          (child) => child.id === selectedItem
        );
        if (foundChild) {
          selectCategory = foundChild;
          break;
        }
      }
      console.log(selectCategory.name);
      if (selectCategory) {

          const filteredProducts = this.products.filter(product => product.category === selectCategory.name);
          this.products = filteredProducts;
      } else {
          console.log("No category selected.");
          // Handle the case where no category is selected
      }
    },
    getProductList(pageNumber, search) {
      if (search === undefined || pageNumber === undefined) {
        search = "";
      }

      let link = `product/list?page=${pageNumber}&search=${search}`;
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          if (response.status == 200) {
            this.products = response.data.products;
            this.pages = response.data.total_pages;
            this.totalPoruducts = response.data.total;
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    next(page) {
      this.getProductList(page);
    },
  },
  created() {
    this.getProductList(1);
  },
};
</script>