<template>
  <div class="d-flex">
    <nav-panel />
    <v-card>
      <div>
        <v-switch
          v-model="postData"
          label="Уведомлять о новых изменениях"
        ></v-switch>
      </div>
      <div>
        <div v-for="item in data" :key="item.pk">
          {{ item.name }}
        </div>
      </div>
    </v-card>

  </div>
</template>

<script>

import NavPanel from "@/components/NavPanel.vue";
export default {
  name: "accountPage",
  components: {NavPanel},
  data() {
    return {
      apiPath: 'api-token-auth/',
      data: [],
      headers: [],
      postData: false,
    }
  },
  mounted() {
      const fetchData = async () => {
      try {
        const token = localStorage.getItem('token');
        const headers = {
          Authorization: `Token ${token}` // Include CSRF token in the headers
        };
        console.log(headers);
        const { data } = await this.$ajax.post(this.apiPath, { headers });
        this.data = data;
        console.log(this.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  },
  methods: {

  }
}
</script>

<style scoped>

</style>