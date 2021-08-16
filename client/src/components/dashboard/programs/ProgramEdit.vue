<template>
  <div
    class="modal fade"
    id="exampleModal"
    tabindex="-1"
    aria-labelledby="exampleModalLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-lg">
      <div class="modal-content">
        <div class="modal-body">
          <div class="d-flex justify-content-between">
            <h2 class="mb-4">Create a referral program</h2>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <form @submit="createProgram">
            <div class="mb-3">
              <label for="program-name" class="form-label">Program Name</label>
              <input
                type="text"
                v-model="name"
                class="form-control input-field"
                id="program-name"
                required="true"
              />
            </div>
            <div class="mb-3">
              <label for="incentive" class="form-label">Incentive</label>
              <input
                v-model="incentive"
                type="number"
                class="form-control input-field"
                id="password"
                required="true"
              />
            </div>
            <button type="submit" class="btn mt-2">Create</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
</style>