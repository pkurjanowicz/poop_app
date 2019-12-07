<template>
    <div>
    <h1>Top Liked Poops</h1>
        <span v-for='(poop, index) in poops' :key='index'>{{poop}}</span>
    </div>
</template>


<script>
export default {
    name: 'topRated',
    props: ['poops'],
    // data() {
    //     return {
    //         poops: '',
    //     }
    // }
}
</script>