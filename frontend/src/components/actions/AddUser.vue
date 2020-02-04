<template>
    <v-container>
        <v-row justify="space-between">
            <v-form ref="form">
                <v-text-field label="Name" v-model="newName"/>
                <v-text-field label="Password" type="password" v-on:keyup.enter="submit" v-model="newPassword"/>
                <v-btn class="mr-4" @click="submit">submit</v-btn>
            </v-form>
        </v-row>
    </v-container>
</template>

<script>
    import {add_user} from '../../inventory'
    export default {
        name: "AddUser",
        data() {
            return {
                newName: "",
                newPassword: ""
            }
        },
        methods: {
            async submit() {
                let resp = await add_user(window.currentPassord, this.newName, this.newPassword);
                if (resp["status"] === "good") {
                    this.$router.go(-1);
                }
            }
        }
    }
</script>

<style scoped>

</style>