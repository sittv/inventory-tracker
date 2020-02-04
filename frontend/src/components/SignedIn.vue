<template>
    <v-app>
        <v-app-bar app
                   color="indigo"
                   dark>
            <!--            <v-app-bar-nav-icon @click.stop="drawer = !drawer"/>-->
            <v-btn icon @click="goHome"><v-icon>mdi-home</v-icon></v-btn>
            <v-toolbar-title>SITTV Inventory</v-toolbar-title>
            <v-spacer/>
            <v-btn icon @click="logout">
                <v-icon>mdi-exit-to-app</v-icon>
            </v-btn>
        </v-app-bar>

        <v-content>
              <router-view></router-view>
        </v-content>


    </v-app>
</template>

<script>

    export default {
        name: "SignedIn",
        components: {},
        mounted() {
            if (window.currentPassord == null || window.currentPassord === "") {
                this.$router.push("/");
            }
        },
        methods: {
            logout() {
                window.currentPassord = null;
                this.$router.push("/");
            },
            goHome() {
                this.$router.push("/signed_in");
            }
        }
    }
</script>

