<template>
    <h2>login Page</h2>
</template>

<script>
export default {
    layout:"loginDefault",
    created(){
        console.log("hey")
        this.$http.post("http://172.20.10.8:8080/auth",{username:"john",password:"hello"})
    }

}
</script>

<style>

</style>