<template>
  <v-data-table
    :headers="headers"
    :items="sliders"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>Sliders</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="1000px" :key="dialogKey">
          <template v-slot:activator="{}">
            <v-btn color="primary" dark class="mb-2" @click="openForm()">
              New Slider
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-form ref="form">
                <v-row>
                  <v-col cols="12" sm="12" md="12">
                    <v-text-field
                      v-model="slider.header"
                      label="Header"
                      :rules="control"
                        required
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
                      v-model="slider.altText"
                      :rules="control"
                        required
                      label="Image Alt text"
                      :prepend-icon="aiIconAlttext"
                      @click:prepend="getAiAlttext()"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="12">
                    <v-select
                      v-model="slider.route"
                      :rules="control"
                        required
                      label="Route"
                      :items="['/shop', '/products', '/collection']"
                    ></v-select>
                  </v-col>
                </v-row>
              </v-form>
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
              >Are you sure you want to delete this slider?</v-card-title
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
      <v-icon small @click="deleteItem(item)"> mdi-delete </v-icon>
    </template>
  </v-data-table>
</template>
    
   <script>
export default {
  layout: "adminDefault",
  name: "adminPage",
  data() {
    return {
      control: [(v) => !!v || "Required!"],
      sliders: [],
      slider: {
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
    this.getSliderList();
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New Slider" : "Edit Slider";
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
    openForm() {
      this.dialogKey = new Date().getTime();
      for (var member in this.slider) delete this.slider[member];
      this.dialog = true;
    },
    editItem(item) {
      this.dialogKey = new Date().getTime();
      this.editedIndex = this.sliders.indexOf(item);
      this.slider = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.sliders.indexOf(item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      let id = this.sliders[this.editedIndex]._id;
      let link = "homepage/delete/" + id;
      this.$store.dispatch("requestDelete", link).then((response) => {
        if (response.status === 200) {
          this.getSliderList();
        } else {
          alert("alert");
        }
      });
      this.closeDelete();
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
      if (this.$refs.form.validate()) {
        if (this.editedIndex > -1) {
          if (this.fileRecords.length > 0) {
            this.slider.imgUrl = this.fileRecords[0].file.name;
          }
          let slider = JSON.parse(JSON.stringify(this.slider));
          let link = "homepage/update/" + this.slider._id;
          let send = { link, data: slider };
          this.$store.dispatch("requestPut", send).then((response) => {
            if (response.status == 200) {
              this.getSliderList();
            } else {
              alert("Error");
            }
          });
        } else {
          this.slider.imgUrl = this.fileRecords[0].file.name;
          let slider = JSON.parse(JSON.stringify(this.slider));
          let link = "homepage/addslider";
          let send = { link, data: slider };
          this.$store.dispatch("requestPost", send).then((response) => {
            if (response.status === 201) {
              this.getSliderList();
            } else {
            }
          });
        }
        this.dialogKey = new Date().getTime();
        this.close();
      }
    },
    async getAiAlttext() {
      this.aiIconAlttext = "mdi-loading";
      let keyWords = { key_words: "Gift" };
      let link = "openai/alttextslider";
      let send = { link, data: keyWords };
      try {
        const response = await this.$store.dispatch("requestPost", send);
        if (response.status === 201) {
          this.slider.altText = response.body.msg.split('"')[1];
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
</script>
    
   <style></style>