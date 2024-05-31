<template>
  <div style="height: inherit">
    <v-card style="height: 100%">
      <v-navigation-drawer
        permanent
        expand-on-hover
      >
        <v-list>
          <v-list-item class="px-2">
            <v-list-item-avatar>
              <v-img src="https://static.tildacdn.com/tild6263-3463-4736-b162-353030396131/_.png"></v-img>
            </v-list-item-avatar>
             <v-list-item-title class="text-h6">
                pseudo-alfadoc
             </v-list-item-title>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list
          nav
          dense
        >
          <router-link to="/user" class="nav-el">
            <v-list-item link>
                <v-list-item-icon>
                  <v-icon>mdi-account</v-icon>
                </v-list-item-icon>
                <v-list-item-title>Профиль</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link to="/current-data" class="nav-el">
            <v-list-item link>
                <v-list-item-icon>
                  <v-icon>mdi-table</v-icon>
                </v-list-item-icon>
                <v-list-item-title>Сертификаты</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link to="/change-data" class="nav-el">
            <v-list-item link>
              <v-list-item-icon>
                <v-icon>mdi-table-headers-eye</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Изменения</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link to="/current-data" class="nav-el">
            <v-list-item link>
                <v-list-item-icon>
                  <v-icon>mdi-shield-key-outline</v-icon>
                </v-list-item-icon>
                <v-list-item-title>СЗИ</v-list-item-title>
            </v-list-item>
          </router-link>

          <router-link to="" class="nav-el">
            <v-list-item link>
              <v-list-item-icon>
                <v-icon>mdi-cog</v-icon>
              </v-list-item-icon>
              <v-list-item-title>Функции</v-list-item-title>
            </v-list-item>
          </router-link>
        </v-list>

        <v-divider></v-divider>

        <v-list style="margin-top: auto">
          <v-list-item class="px-2">
            <v-list-item-avatar>
              <v-img src="https://randomuser.me/api/portraits/women/85.jpg"></v-img>
            </v-list-item-avatar>
          </v-list-item>

          <v-list-item link>
            <v-list-item-content>
              <v-list-item-title class="text-h6">
                <v-icon
                    @click="onLogout"
                >
                  mdi-exit-to-app
                </v-icon>
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>


      </v-navigation-drawer>
    </v-card>
  </div>
</template>
<script>

export default {
  name: "NavPanel",
  methods: {
    onLogout() {
        this.$store.commit('login/removeToken')
        this.$router.push('/login')
    }
  }

}
</script>
<style scoped>
  .nav-el {
    text-decoration: none;
  }
</style>