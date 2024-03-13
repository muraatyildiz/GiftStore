<template>
  <v-data-table
    :headers="headers"
    :items="users"
    sort-by="calories"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar flat>
        <v-toolbar-title>User List</v-toolbar-title>
        <v-divider class="mx-4" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="1000px" :key="dialogKey">
          <template v-slot:activator="{}">
            <v-btn color="primary" dark class="mb-2" @click="openForm()">
              New User
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
                      v-model="user.username"
                      label=" Username"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model="user.password"
                      label="Password"
                      :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                      :type="showPassword ? 'text' : 'password'"
                      @click:append="showPassword = !showPassword"
                      :disabled="editedIndex !== -1"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model="user.fullname"
                      label=" Full name"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-select
                      v-model="user.role"
                      label="Role"
                      :items="['admin', 'manager', 'staff', 'guest','customer']"
                    ></v-select>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model.number="user.phonenumber"
                      label="Phone Number"
                      type="number"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="12" sm="12" md="6">
                    <v-text-field
                      v-model="user.email"
                      label="Email"
                      type="email"
                    ></v-text-field>
                  </v-col>
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
                >Are you sure you want to delete this user?</v-card-title
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
  name: "adminPage",
  data() {
    return {
      users: [],
      user: {
        id: "",
        username: "",
        password: "",
        phonenumber: "",
        fullname: "",
        email: "",
        role: "",
      },
      headers: [
        { text: "Username", value: "username" },
        { text: "Full Name", value: "fullname" },
        { text: "Phone Number", value: "phonenumber" },
        { text: "Email", value: "email" },
        { text: "Role", value: "role" },
        { text: "Actions", value: "actions", sortable: false },
      ],
      dialog: false,
      dialogKey: new Date().getTime(),
      editedIndex: -1,
      showPassword: false,
      dialogDelete: false
    };
  },
  created() {
    this.getUserList();
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "New User" : "Edit User";
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
    getUserList() {
      let link = "auth/userList";
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          var answer = response.body;
          if (response.status == 200) {
            this.users = answer;
          }
        })
        .catch((x) => {
          console.log("Error");
        });
    },
    openForm() {
      this.dialogKey = new Date().getTime();
      for (var member in this.user) delete this.user[member];
      this.dialog = true;
    },
    editItem(item) {
      this.dialogKey = new Date().getTime();
      this.editedIndex = this.users.indexOf(item);
      this.user = Object.assign({}, item);
      this.dialog = true;
    },

    deleteItem(item) {
      this.editedIndex = this.users.indexOf(item);
      this.dialogDelete = true;
    },

    deleteItemConfirm() {
      let id = this.users[this.editedIndex]._id;
      let link = "auth/delete/" + id;
      this.$store.dispatch("requestDelete", link).then((response) => {
        if (response.status === 200) {
          this.getUserList();
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
      if (this.editedIndex > -1) {
        let user = JSON.parse(JSON.stringify(this.user));
        let link = "auth/update/"+ this.user._id;
        let send = { link, data: user };
        this.$store.dispatch("requestPut", send).then((response) => {
          if (response.status == 200) {
            this.getUserList();
          } else {
            alert("Error");
          }
        });
      } else {
        let user = JSON.parse(JSON.stringify(this.user));
        let link = "auth/add";
        let send = { link, data: user };
        this.$store.dispatch("requestPost", send).then((response) => {
          if (response.status === 201) {
            this.getUserList();
          } else {
          }
        });
      }
      this.dialogKey = new Date().getTime();
      this.close();
    },
  },
};
</script>
  
 <style></style>