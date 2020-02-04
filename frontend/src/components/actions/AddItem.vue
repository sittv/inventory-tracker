<template>
    <v-container>
        <v-row justify="space-between">
            <v-form ref="form">
                <v-text-field label="Item Name" v-model="itemName"/>
                <v-text-field label="Location" v-model="itemLocation"/>
                <v-text-field label="Barcode" v-model="itemBarcode"/>
                <v-btn class="mr-4" @click="submit">submit</v-btn>
            </v-form>
        </v-row>
    </v-container>
</template>

<script>
    import {add_item} from '../../inventory'
    export default {
        name: "AddItem",
        data() {
            return {
                itemName: "",
                itemLocation: "",
                itemBarcode: ""
            }
        },
        methods: {
            async submit() {
                let resp = await add_item(window.currentPassord, this.itemName, this.itemLocation, this.itemBarcode);
                if (resp["status"] === "good") {
                    this.$router.go(-1);
                }
            }
        }
    }
</script>

<style scoped>

</style>