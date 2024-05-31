<template>
  <div class="d-flex gap-1">
    <div class="d-flex align-center gap-0">
      <span>Дата начала</span>
      <v-text-field
          outlined
          dense
          hide-details
      />
    </div>

     <div class="d-flex align-center gap-0">
      <span>Дата конца</span>
      <v-text-field
          outlined
          dense
          hide-details
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "DateFilter"
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