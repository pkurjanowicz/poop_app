<template>
    <span class='badge'>{{content}}</span>
</template>

<script>
export default {
    name: "buttonBadge",
    props: ['content'],
}
</script>

<style scoped>
.badge {
    background-color: rgb(167, 0, 0);
    color: white;
    border-radius: 50%;
    width: 10px;
    height: 10px; 
    font-size: 12px;
    position: relative;
    right: 7px;
    top: 14px;
}
</style>


