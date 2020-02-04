<template>
    <!--    <div>-->
    <!--        <p>Swipe Your card or type code to login</p>-->
    <!--        <p v-show="badLogin" class="badLogin">Password Incorrect</p>-->
    <!--        <input type="password" ref="password" placeholder="type code here" v-model="code" v-on:keyup.enter="checkPassword"/>-->
    <!--    </div>-->

    <v-app>
        <v-content>
            <v-container
                    class="fill-height"
                    fluid
            >
                <v-row
                        align="center"
                        justify="center"
                >
                    <v-col
                            cols="12"
                            sm="8"
                            md="4"
                    >
                        <v-card class="elevation-12">
                            <v-toolbar flat>
                                <v-toolbar-title>SITTV Inventory Login</v-toolbar-title>
                                <v-spacer/>
                            </v-toolbar>
                            <v-card-text>
                                <p v-show="badLogin" class="badLogin">Password Incorrect</p>

                                <v-form>
                                    <v-text-field
                                            label="Password"
                                            prepend-icon="mdi-lock"
                                            type="password"
                                            v-model="code"
                                            v-on:keyup.enter="checkPassword"
                                            ref="password"
                                    />
                                </v-form>
                            </v-card-text>
                            <v-card-actions>
                                <v-btn>Create Account</v-btn>
                                <v-spacer/>
                                <v-btn color="primary" @click="checkPassword">Login</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
        </v-content>
    </v-app>
    <!--    <p><router-link to="/login">Login</router-link></p>-->
    <!--    <p><router-link to="/Browse">Browse Inventory</router-link></p>-->
</template>

<script>

    import * as api from "../inventory";

    export default {
        name: "HomePage",
        data() {
            return {
                code: "",
                badLogin: false
            }
        },
        mounted() {
            this.$refs.password.focus();
        },
        methods: {
            async checkPassword() {
                let good = await api.check_login(this.code);
                this.badLogin = !good;
                if (good) {
                    window.currentPassord = this.code;
                    await this.$router.push("signed_in");
                }
                this.code = "";
            }
        }
    }
</script>

<style scoped>
    .badLogin {
        color: red;
        font-weight: bold;
    }

</style>