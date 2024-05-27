<template>
  <v-sheet class="bg-deep-purple pa-12" rounded>
    <v-card class="mx-auto px-6 py-8" max-width="344">
      <p class="justify-center d-flex text-h5">Вход</p>
      <v-form
        v-model="form"
        @submit.prevent="onSubmit"
      >
        <v-text-field
          v-model="username"
          :readonly="loading"
          :rules="[required]"
          label="Логин"
          clearable
          outlined
        />

        <v-text-field
          v-model="password"
          :readonly="loading"
          :rules="[required]"
          :type="'password'"
          label="Пароль"
          placeholder="Введите пароль"
          clearable
          outlined
        />

        <v-btn
          :disabled="!form"
          :loading="loading"
          color="primary"
          size="large"
          type="submit"
          variant="elevated"
          block
        >
          Войти
        </v-btn>
      </v-form>
    </v-card>
  </v-sheet>
</template>

<script>

import {mapActions} from "vuex";

export default {
  name: "loginPage",
  data() {
    return {
      username: null,
      password: null,
      loading: false,
      form: false,
    }
  },
  methods: {
    ...mapActions(['login/login']),
    loginUser () {
      this['login/login']({username: this.username, password: this.password, router: this.$router})
    },
    onSubmit () {
        if (!this.form) return

        this.loading = true

        setTimeout(() => (this.loading = false), 2000)
        this.loginUser()
      },
      required (v) {
        return !!v || 'Необходимо ввести данные!'
    },
  }
}
</script>

<style scoped>

</style>