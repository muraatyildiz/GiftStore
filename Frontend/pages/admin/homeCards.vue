<template>

      <v-data-table
        :headers="headers"
        :items="cards"
        sort-by="calories"
        class="elevation-1"
      >
        <template v-slot:top>
          <v-toolbar flat>
            <v-toolbar-title>Home Page Image Cards</v-toolbar-title>
            <v-divider class="mx-4" inset vertical></v-divider>
            <v-spacer></v-spacer>
            <v-dialog v-model="dialog" max-width="1000px" :key="dialogKey">
              <v-card>
                <v-card-title>
                  <span class="text-h5">{{ formTitle }}</span>
                </v-card-title>
  
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12" sm="12" md="12">
                        <v-text-field
                          v-model="card.header"
                          label="Header"
                        ></v-text-field>
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
                          v-model="card.altText"
                          label="Image Alt text"
                          :prepend-icon="aiIconAlttext"
                          @click:prepend="getAiAlttext()"
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12" sm="12" md="12">
                        <v-select
                          v-model="card.route"
                          label="Route"
                          :items="['/shop', '/products', '/collection']"
                        ></v-select>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
  
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="blue darken-1" text @click="close">
                    Cancel
                  </v-btn>
                  <v-btn color="blue darken-1" text @click="save"> Save </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-toolbar>
        </template>
        <template v-slot:item.imgUrl="{ item }">
          <v-img
            :src="$store.state.ApiLink + 'file/serve-image/' + item.imgUrl"
            width="100"
            height="75"
            contain
          ></v-img>
        </template>
        <template v-slot:item.actions="{ item }">
          <v-icon small class="mr-2" @click="editItem(item)"> mdi-pencil </v-icon>
       
        </template>
      </v-data-table>
   
  </template>
      
     <script>
  export default {
    layout: "adminDefault",
    name: "adminPage",
    data() {
      return {
        cards: [],
        card: {
          id: "",
          header: "",
          imgUrl: "",
          altText: "",
          route: "",
        },
    
        fileRecordsForUpload: [],
        fileRecords: [],
        headers: [
          { text: "Header", value: "header" },
          { text: "Image", value: "imgUrl" },
          { text: "image Alt text", value: "altText" },
          { text: "Route", value: "route" },
          { text: "Actions", value: "actions", sortable: false },
        ],
        dialog: false,
      
        dialogKey: new Date().getTime(),
       
        editedIndex: -1,
        showPassword: false,
        dialogDelete: false,
        aiIconAlttext: "mdi-search-web",
      };
    },
    created() {
      this.getCardList();
      
    },
    computed: {
      formTitle() {
        return "Edit Card";
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
    methods: {
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
      openForm() {
        this.dialogKey = new Date().getTime();
        for (var member in this.card) delete this.card[member];
        this.dialog = true;
      },
      editItem(item) {
        this.dialogKey = new Date().getTime();
        this.editedIndex = this.cards.indexOf(item);
        this.card = Object.assign({}, item);
        this.dialog = true;
      },
      close() {
        this.dialogKey = new Date().getTime();
        this.dialog = false;
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
      
          if (this.fileRecords.length > 0) {
            this.card.imgUrl = this.fileRecords[0].file.name;
          }
          let card = JSON.parse(JSON.stringify(this.card));
          let link = "homepage/updatecard/" + this.card._id;
          let send = { link, data: card };
          this.$store.dispatch("requestPut", send).then((response) => {
            if (response.status == 200) {
              this.getCardList();
            } else {
              alert("Error");
            }
          });
    
        this.dialogKey = new Date().getTime();
        this.close();
      },
  
      async getAiAlttext() {
        this.aiIconAlttext = "mdi-loading";
        let keyWords = { key_words: "Gift" };
        let link = "openai/alttextslider";
        let send = { link, data: keyWords };
        try {
          const response = await this.$store.dispatch("requestPost", send);
          if (response.status === 201) {
            this.card.altText = response.body.msg.split('"')[1];
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
  </script>x
      
     <style></style>