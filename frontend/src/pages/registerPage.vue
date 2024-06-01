<template>
  <v-sheet class="bg-deep-purple pa-12 stealer" rounded>
    <div class="banner__abs"></div>
    <div class="banner__abs"></div>
    <div class="banner__abs"></div>
    <div class="banner__abs"></div>
    <div class="banner__abs"></div>
    <v-card class="mx-auto px-6 py-8" max-width="344" style="margin-top: 10%;">
      <span class="d-flex" style="padding-bottom: 16px">
        <router-link to="/login">
            <v-btn
            :loading="loading"
            color="#FECE09"
            size="large"
            variant="elevated"
          >
            <v-icon>
              mdi-arrow-left
            </v-icon>
          </v-btn>
        </router-link>
        <p class="justify-center d-flex text-h5" style="margin-left: 20px;">Регистрация</p>
      </span>

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
          dense
        />

        <v-text-field
          v-model="email"
          :readonly="loading"
          :rules="[required]"
          label="Почта"
          clearable
          outlined
          dense
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
          dense
        />

        <v-btn
          :disabled="!form"
          :loading="loading"
          color="black"
          size="large"
          type="submit"
          variant="elevated"
          block
          class="login-btn"
        >
          Зарегистрироваться
        </v-btn>
      </v-form>
    </v-card>
  </v-sheet>
</template>

<script>

import {mapActions} from "vuex";

export default {
  name: "registerPage",
  data() {
    return {
      username: null,
      password: null,
      email: null,
      loading: false,
      form: false,
    }
  },
  methods: {
    ...mapActions(['login/register']),
    loginUser () {
      this['login/register']({username: this.username, email: this.email, password: this.password, router: this.$router})
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
  .theme--light.v-btn.v-btn--disabled.v-btn--has-bg {
    background-color: black !important;
    color: #8c8c8c !important;
  }
  .login-btn {
    background-color: black;
    border: 1px solid black;
    color: #fff;
    text-transform: capitalize;
    width: 77%;
  }
  .login-btn:hover {
    border: 2px solid #FECE09;
  }
  .stealer {
    min-height: 100vh;
    background: #000;
    background-image: url("https://alfa-doc.ru/images/bbg.png");
    background-repeat: no-repeat;
    background-position: top right;
  }
  .banner__abs:first-child {
    left: 165px;
    bottom: 624px;
    animation-name: banner-1;
    animation-duration: 10s;
  }
  .banner__abs:nth-child(2) {
    left: 400px;
    bottom: 100px;
    animation-name: banner-2;
    animation-duration: 14s;
  }
  .banner__abs:nth-child(3) {
    left: unset;
    right: 594px;
    bottom: 384px;
    animation-name: banner-3;
    animation-duration: 11s;
  }
  .banner__abs:nth-child(4) {
    left: unset;
    right: 165px;
    bottom: 193px;
    animation-name: banner-4;
    animation-duration: 15s;
  }
  .banner__abs:nth-child(5) {
    left: unset;
    right: 50%;
    bottom: 0;
    animation-name: banner-5;
    animation-duration: 20s;
  }
  .banner__abs {
    content: '';
    position: absolute;
    width: 1px;
    height: 122px;
    background: linear-gradient(151deg, #FECE09 0%, rgba(254, 206, 9, 0.00) 100%);
    animation-timing-function: linear;
    animation-iteration-count: infinite;
  }
  @keyframes banner-1 {
    0% {
      top: 624px;
      opacity: 1;
    }
    50% {
      top: 0;
      opacity: 0;
    }
    51% {
      top: 100%;
      opacity: 1;
    }
    100% {
      top: 624px;
    }
  }
  @keyframes banner-2 {
    0% {
      top: 100%;
    }
    100% {
      top: 0;
    }
  }
  @keyframes banner-3 {
    0% {
        top: 384px;
        opacity: 1;
    }
    50% {
        top: 0;
        opacity: 0;
    }
    51% {
        top: 100%;
        opacity: 1;
    }
    100% {
        top: 384px;
    }
  }

  @keyframes banner-4{
    0% {
        top: 193px;
        opacity: 1;
    }
    50% {
        top: 0;
        opacity: 0;
    }
    51% {
        top: 100%;
        opacity: 1;
    }
    100% {
        top: 193px;
    }
  }
  @keyframes banner-5 {
    0% {
        top: 100%;
    }
    100% {
        top: 0;
    }
  }
</style>