<script>
</script>

<main class="text-neutral-900">
  <div id="container" class="px-8 sm:px-20 md:px-40 lg:px-80">
    <div id="title" class="py-10 w-full">
      <h1 class="text-6xl text-center">Fur Dictionary</h1>
    </div>

    <div id="search" class="py-10 flex flex-row place-content-evenly">
      <input
        class="text-4xl p-4 bg-transparent placeholder:text-neutral-600 outline-none border-b-2 border-transparent focus:border-neutral-900 focus:placeholder:text-transparent"
        placeholder="Search for a word"
      />
      <button
        class="text-4xl p-4 bg-neutral-700 hover:bg-neutral-600 text-neutral-200 transition-colors ease-in"
        >Go</button
      >
    </div>

    <div id="result" class="py-10">
      <span id="word" class="font-bold">ABCDEFGHIJ</span>:
      <span id="definition">ABCDEFGHIJKLMNOPQRSTUVWX</span>
    </div>
  </div>
</main>
