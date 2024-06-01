<template>
  <div class="d-flex">
    <nav-panel />
    <v-card class="account">
      <span style="font-size: 24px">Профиль</span>
      <div>
        <div class="d-flex flex-column">
          <div class="d-flex flex-column">
            <span class="name">Имя</span>
            <span class="data">{{ data.name }}</span>
          </div>

          <div class="d-flex flex-column">
            <span class="name">Фамилия</span>
            <span class="data">{{ data.surname }}</span>
          </div>

          <div class="d-flex flex-column">
            <span class="name">Отчество</span>
            <span class="data">{{ data.patronymic }}</span>
          </div>

          <div class="d-flex flex-column">
            <span class="name">Почта</span>
            <span class="data">{{ data.user.email }}</span>
          </div>

          <div class="d-flex flex-column">
            <span class="name">О себе</span>
            <span class="data">{{ data.bio }}</span>
          </div>

          <div class="d-flex flex-column">
            <span class="name">Роль</span>
            <span class="data">{{ data.post }}</span>
          </div>

        </div>
      </div>
      <div>
        <v-switch
          v-model="isManage"
          inset
          label="Является менеджером"
          @change="changeState()"
        ></v-switch>
      </div>
      <div>
        <v-switch
          v-model="postData"
          inset
          label="Уведомлять о новых изменениях"
          @change="changeState()"
        ></v-switch>
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
      isManage: false,
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
        this.postData = this.data.notify_me
        this.isManage = this.data.manager
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  },
  methods: {
    changeState() {
      this.data.notify_me = this.postData
      this.data.manager = this.isManage
      this.$ajax.post(`${this.apiPath}/`, {...this.data})
    }
  }
}
</script>

<style scoped>
 .account {
   width: calc(100% - 120px);
   height: calc(100vh - 50px);
   margin: auto;
   padding: 32px;
 }
 .name {
   padding: 12px 8px;

 }
 .data {
   background-color: #efefef;
   border-radius: 2px;
   padding: 12px;
   border: 1px solid #b9b9b9;
 }
</style>