

<template>
  <v-data-table
    :headers="headers"
    :items="products"
    sort-by="name"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Product List</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="1000px" :key="dialogKey">
          <template v-slot:activator="{}">
            <v-btn color="primary" dark class="mb-2" @click="openForm()">
              New Product
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model="product.name"
                      label="Product Name"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model.number="product.price"
                      label="Price"
                      prefix="€"
                      type="number"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-select
                      v-model="product.category"
                      label="Category"
                      :items="['flowers', 'christmas', 'event']"
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model.number="product.stock"
                      label="Stock"
                      type="number"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <v-textarea
                      clearable
                      clear-icon="mdi-close-circle"
                      :prepend-icon="aiIconDescription"
                      v-model="product.description"
                      label="Description"
                      variant="outlined"
                      color="cyan"
                      @click:prepend="getAiDescription()"
                      placeholder="Get Ai support for product decription"
                    ></v-textarea>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <div>
                      <VueFileAgent
                        ref="vueFileAgent"
                        :theme="'grid'"
                        :multiple="true"
                        :deletable="true"
                        :meta="true"
                        :maxSize="'10MB'"
                        :linkable="true"
                        :maxFiles="1"
                        @beforedelete="onBeforeDelete($event)"
                        :helpText="'Choose img for the product'"
                        :errorText="{
                          type: 'Invalid file type. Only images or zip Allowed',
                          size: 'Files should not exceed 10MB in size',
                        }"
                        @select="filesSelected($event)"
                        @delete="fileDeleted($event)"
                        :disabled="false"
                        v-model="fileRecords"
                        accept="image/*"
                      >
                      </VueFileAgent>
                    </div>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <v-text-field
                      v-model="product.altText"
                      label="Image Alt text"
                      :prepend-icon="aiIconAlttext"
                      @click:prepend="getAiAlttext()"   
                    ></v-text-field>
                  </v-col>
                  <!-- <v-col cols="12" sm="12" md="12">
                      <v-img
                      
                        src="http://192.168.0.63:8080/file/serve-image/bolt-dumbbells-1.jpg" 
                      ></v-img>
                    </v-col> -->
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close"> Cancel </v-btn>
              <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="800px">
          <v-card>
            <v-card-title class="text-h5"
              >Are you sure you want to delete this product?</v-card-title
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete"
                >Cancel</v-btn
              >
              <v-btn color="blue darken-1" text @click="deleteItemConfirm"
                >OK</v-btn
              >
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
      <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>
  </v-data-table>
</template>
  
  <script>
export default {
  layout: "adminDefault",
  name: "productListPage",
  data: () => ({
    product: {
      id: "",
      name: "",
      category: "",
      stock: null,
      price: null,
      imgUrl: "",
      altText: "",
      description: "",
      userId: "",
    },
    dialog: false,
    dialogDelete: false,
    fileRecordsForUpload: [],
    fileRecords: [],
    headers: [
      {
        text: "Products",
        align: "start",
        sortable: false,
        value: "name",
      },
      { text: "Price", value: "price" },
      { text: "Stock", value: "stock" },
      { text: "Description", value: "description" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    dialogKey: new Date().getTime(),
    products: [],
    editedIndex: -1,
    aiIconDescription: "mdi-search-web",
    aiIconAlttext: "mdi-search-web",
  }),

  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Product" : "Edit Product";
    },
  },

  watch: {
    dialog(val) {
      val || this.close();
      this.dialogKey = new Date().getTime();
    },
    dialogDelete(val) {
      val || this.closeDelete();
    },
  },

  created() {
    this.getProductList();
  },
  methods: {
    getProductList() {
      let link = "product/admin/list";
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          if (response.status == 200 ) {
            this.products = response.data.products;
          }
        })
        .catch((x) => {
          console.log("Error");
        });
    },
    openForm() {
      this.dialogKey = new Date().getTime();
      for (var member in this.product) delete this.product[member];
      this.fileRecords = [];
      this.dialog = true;
    },
    editItem(item) {
      this.dialogKey = new Date().getTime();
      this.editedIndex = this.products.indexOf(item);
      this.product = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.products.indexOf(item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      let id = this.products[this.editedIndex]._id;
      let link = "product/delete/" + id;
      this.$store.dispatch("requestDelete", link).then((response) => {
        var answer = response.body;
        this.getProductList();
      });
      this.closeDelete();
    },
    close() {
      this.dialog = false;
      this.dialogKey = new Date().getTime();
      this.$nextTick(() => {
        this.editedIndex = -1;
      });
    },

    closeDelete() {
      this.dialogDelete = false;
      this.$nextTick(() => {
        this.editedIndex = -1;
      });
    },

    save() {
      if (this.editedIndex > -1) {
        if (this.fileRecords.length > 0) {
          this.product.imgUrl = this.fileRecords[0].file.name;
        }
        let product = JSON.parse(JSON.stringify(this.product));
        let id = this.products[this.editedIndex]._id;
        let link = "product/update/" + id;
        let send = { link, data: product };
        this.$store.dispatch("requestPut", send).then((response) => {
          if ((response.status = 200)) {
            this.getProductList();
          } else {
          }
        });
      } else {
        this.product.imgUrl = this.fileRecords[0].file.name;
        let product = JSON.parse(JSON.stringify(this.product));
        let link = "product/add";
        let send = { link, data: product };
        this.$store.dispatch("requestPost", send).then((response) => {
          if (response.status == 201) {
            this.getProductList();
          } else {
          }
        });
      }
      this.dialogKey = new Date().getTime();
      this.close();
    },
    async getAiDescription() {
      this.aiIconDescription = "mdi-loading";
      let keyWords = { key_words: this.product.name };
      let link = "openai/description";
      let send = { link, data: keyWords };
      await this.$store.dispatch("requestPost", send).then((response) => {
        if (response.status === 201) {
          this.product.description = response.body.msg.split('"')[1];
        } else {
        }
      });
      this.aiIconDescription = "mdi-search-web";
    },
    async getAiAlttext() {
      this.aiIconAlttext = "mdi-loading";
      let keyWords = { key_words: this.product.name };
      let link = "openai/alttext";
      let send = { link, data: keyWords };
      try {
        const response = await this.$store.dispatch("requestPost", send);
        if (response.status === 201) {
         this.product.altText = response.body.msg.split('"')[1];
        } else {
          return null;
        }
      } catch (error) {
        console.error("Error:", error);
        return null;
      }
      this.aiIconAlttext = "mdi-search-web";
    },

filesSelected: async function (fileRecordsNewlySelected) {
      var validFileRecords = fileRecordsNewlySelected.filter(
        (fileRecord) => !fileRecord.error
      );

      this.fileRecordsForUpload =
        this.fileRecordsForUpload.concat(validFileRecords);
      let link = this.$store.state.ApiLink + "file/upload";
      let Token = "Bearer ";
      this.$refs.vueFileAgent
        .upload(link, { Authorization: Token }, this.fileRecordsForUpload)
        .then((f) => {
          this.fileRecordsForUpload = [];
       
         
        
        });
      console.log("files", this.fileRecordsForUpload);
    },
    fileDeleted: function (fileRecord) {
      console.log("here");
    },
    onBeforeDelete: function (fileRecord) {
      var i = this.fileRecordsForUpload.indexOf(fileRecord);
      console.log("here2");
    },
  },
};
</script>
   
  <style></style>
  