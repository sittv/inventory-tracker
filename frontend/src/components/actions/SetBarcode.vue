<template>
    <v-container>
        <v-row justify="space-between">
            <v-form ref="form">
                <v-text-field label="itemId" v-model="itemId"/>
                <v-text-field label="Barcode" v-model="barcode"/>
                <v-btn class="mr-4" @click="submit">submit</v-btn>
            </v-form>
        </v-row>
    </v-container>
</template>

<script>
    import {id_return} from '../../inventory'
    export default {
        name: "IDReturn",
        data() {
            return {
                itemId: "",
                barcode: ""
            }
        },
        methods: {
            async submit() {
                let resp = await id_return(window.currentPassord, this.itemId);
                if (resp["status"] === "good") {
                    this.$router.go(-1);
                }
            }
        }
    }
</script>

<style scoped>

</style>