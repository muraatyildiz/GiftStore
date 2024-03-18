<template>
    <v-container class="mt-4">
        <v-row align="center"
         justify="center">
            <v-col cols="12" md="5" sm="12">
                <v-card>
                    <v-card-title>
                        <v-toolbar class="blue darken-4">
                            <v-toolbar-title class="white--text"><h4> Sign In </h4></v-toolbar-title>
                            
                        </v-toolbar>
                       
                    </v-card-title>
                    <v-card-text>
                        <v-alert dense v-if="loginError"
                                 outlined
                                 type="error">
                                 The username or password is<strong> incorrect!</strong>
                        </v-alert>
                        
                        <v-form ref="form">
                            <v-row>
                                <v-col cols="12">
                                    <v-text-field v-model="authData.username"
                                                  label="Username"
                                                  :rules="control" required
                                                  type="text " prepend-icon="mdi-account">
                                    </v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-text-field v-model="authData.password"
                                                  label="password"
                                                  :rules="control" required
                                                  type="password" prepend-icon="lock">
                                    </v-text-field>
                                </v-col>
                                <v-col cols="12">
                                    <v-btn block @click.prevent="login" :value="Loading" color="blue darken-4" class="white--text">
                                        login
                                    </v-btn>
                                </v-col>
                            </v-row>
                            <v-overlay :value="Loading">
                                <!-- <v-progress-circular indeterminate size="64" button="false">
                             Loading...
                       </v-progress-circular> -->
                            </v-overlay>
                        </v-form>
                    </v-card-text>
                    <v-card-actions>
                   

                    </v-card-actions>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
    
</template>
<script>
    export default {
        layout: "loginDefault",
        data() {
            return {
                control: [v => !!v || 'Required!'],
                authData: { username: "", password: ""},
                loginError: null,
                Loading:false,


            }
        },
        methods: {
            login() {              
                 var ths = this;
                
                if (this.$refs.form.validate() || this.$route.query.dv) {
                     this.Loading=true;
                    this.$store.dispatch("auth/authUser", this.authData).then((response) => { 
                         this.Loading=false;                     
                    }
                    ).catch(r => {
                        this.$refs.form.reset();
                        this.loginError = true;
                         this.Loading=false;
                    });
                }
            }
        },
        created() {       
            if (process.client) {
                var ths = this;
                let isAuthenticated = this.$store.getters["auth/isAuthenticated"];
                if (isAuthenticated) {
                    this.$router.push("/");
                } else {
                    this.$store.commit("setUserInfo", null);
                }
            }
        },
        mounted() {      
            if (this.$route.query.dv) {
                if (process.client) {
                    this.login();
                }
            }

            if (process.client) {

                setTimeout(x => {


                }, 1000);

            }
      }
    }
</script>