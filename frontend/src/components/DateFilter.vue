<template>
  <div class="d-flex gap-1" style="align-items: center">
    <div class="d-flex align-center gap-0">
      <span>Дата начала</span>
      <v-text-field
          v-model="startDate"
          outlined
          dense
          hide-details
      />
    </div>

     <div class="d-flex align-center gap-0">
      <span>Дата конца</span>
      <v-text-field
          v-model="endDate"
          outlined
          dense
          hide-details
      />
    </div>
    <v-btn
        color="rgba(254, 206, 9, 1)"
        @click="find"
        style="height: 40px"
      >
        Найти
      </v-btn>
  </div>
</template>

<script>
export default {
  name: "DateFilter",
  inject: ['$table'],
  data() {
    return {
      startDate: null,
      endDate: null,
    }
  },
  methods: {
    find() {
      if (this.startDate !== null && this.endDate !== null) {
        this.$table.startDate = this.startDate
        this.$table.endDate = this.endDate
      } else {
        this.startDate = null
        this.endDate = null
      }
    }
  }
}
</script>

<style scoped>
  .gap-0 {
    gap: 4px;
  }
  .gap-1 {
    gap: 8px;
  }
</style>