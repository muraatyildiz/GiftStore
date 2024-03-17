<template>
  <div>
    <v-container>
      <p class="display-3 font-weight-light text-center pa-4">
        User Information
      </p>
      <p class="overline text-center">{{user.fullname}} | "Acount Created Date"</p>
      <div class="row">
        <div class="col-md-12 col-sm-12 col-xs-12">
          <ul class="subtitle-1 font-weight-light">
            <li><b>Username: </b>{{ user.username }}</li>
            <li><b>Phone Number: </b>{{ user.phonenumber }}</li>
            <li><b>Email: </b>{{ user.email }}</li>
            <li v-if="user.role !== 'customer'"><nuxt-link to="/admin"><b>Go to Admin</b></nuxt-link></li>
            <li><nuxt-link to="/admin"><b>Log Out</b></nuxt-link></li>
          </ul>
          <p class="body-1 font-weight-light pt-10"><b>Orders Records</b></p>
          
        </div>
      </div>
    </v-container>
  </div>
</template>
  <script>
export default {
  layout: "userDefault",
  data: () => ({
    rating: 4.5,
    item: 5,
    user:{}
  }),
  methods: {
    getUser() {
      let link = "auth/userInfo";
      this.$store
        .dispatch("requestGet", link)
        .then((response) => {
          if (response.status === 200) {
            this.user = response.body.user;
          }
        })
        .catch((x) => {
          console.log("Error");
        });
    },
  },
  created() {
    this.getUser();
  },
};
</script>
  