<template>
  <div class="d-flex" style="width: 100%">
    <nav-panel />
    <v-card>
      <div>
        <v-switch
          v-model="postData"
          label="Уведомлять о новых изменениях"
          @change="changeState(data.id)"
        ></v-switch>
      </div>
      <div>
        <div class="d-flex flex-column">
          <span>{{ data.name }}</span>
          <span>{{ data.surname }}</span>
          <span>{{ data.patronymic }}</span>
          <span>{{ data.bio }}</span>
          <span>{{ data.post }}</span>
          <span>{{ data.manage }}</span>
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
      apiPath: 'account/account',
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
          Authorization: `Token ${token}`
        };
        const { data } = await this.$ajax.get(this.apiPath, { headers });
        this.data = data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  },
  methods: {
    changeState(id) {
      this.data.notify_me = this.postData
      console.log(this.data)
      this.$ajax.put(`${this.apiPath}${id}`, {...this.data})
    }
  }
}
</script>

<style scoped>

</style>