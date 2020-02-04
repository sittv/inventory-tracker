<template>
    <v-container>
        <v-row justify="space-between">
            <v-form ref="form">
                <v-text-field label="itemId" v-model="itemId"/>
                <v-btn class="mr-4" @click="submit">submit</v-btn>
            </v-form>
        </v-row>
    </v-container>
</template>

<script>
    import {id_checkout} from '../../inventory'
    export default {
        name: "IdCheckout",
        data() {
            return {
                itemId: "",
            }
        },
        methods: {
            async submit() {
                let resp = await id_checkout(window.currentPassord, this.itemId);
                if (resp["status"] === "good") {
                    this.$router.go(-1);
                }
            }
        }
    }
</script>

<style scoped>

</style>