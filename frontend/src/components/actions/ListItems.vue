<template>
    <v-content>
        <v-data-table :headers="headers" :items="data"></v-data-table>
    </v-content>
</template>

<script>
    import {get_items} from "../../inventory"

    export default {
        name: "ListItems",
        data() {
            return {
                headers: [
                    {text: "Item ID", value: "id"},
                    {text: "Name", value: "name"},
                    {text: "Location", value: "location"},
                    {text: "Barcode", value: "barcode"},
                    {text: "In Use", value: "in_use"}
                ],
                data: []
            }
        },
        mounted() {
            get_items().then((data) => {
                this.data = data;
            })
        }
    }
</script>

<style scoped>

</style>