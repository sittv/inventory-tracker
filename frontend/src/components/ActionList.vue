<template>
    <div class="action_list">
        <router-link class="action" to="/signed_in/add_user" tag="div">Add User</router-link>
        <router-link class="action" to="/signed_in/list_items" tag="div">List Items</router-link>
        <router-link class="action" to="/signed_in/add_item" tag="div">Add Item</router-link>
        <router-link class="action" to="/signed_in/id_checkout" tag="div">ID Checkout</router-link>
        <router-link class="action" to="/signed_in/barcode_checkout" tag="div">Barcode Checkout</router-link>
        <router-link class="action" to="/signed_in/set_barcode" tag="div">Set Barcode</router-link>
        <router-link class="action" to="/signed_in/id_return" tag="div">ID Return</router-link>
        <router-link class="action" to="/signed_in/barcode_return" tag="div">Barcode Return</router-link>
        <div class="action" @click="logout">Logout</div>


    </div>
</template>
<script>
    export default {
        name: 'ActionList',
        methods: {
            logout() {
                window.currentPassord = null;
                this.$router.push("/");
            }
        }
    }
</script>
<style scoped>
    .action_list {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        height: 100%;
        width: 100%;

    }

    .action {
        font-size: 3.5vw;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .action:nth-child(odd) {
        background-color: #0f1937;
        color: white;
    }

    .action:nth-child(even) {
        background-color: #c0c6ff;
        color: black;
    }


</style>