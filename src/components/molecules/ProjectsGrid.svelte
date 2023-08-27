<script>
	import Project from '../atoms/Project.svelte';
</script>

<div class="grid-container">
	<div class="grid">
		<!--<Project
			img="roptimiceps.png"
			title="Roptimiceps"
			description="Own modpack tha I created to optimize and improve gameplay of Minecraft"
			buttonText="Modrinth"
			href="https://modrinth.com/modpack/roptimiceps" />--> <!-- TODO When will be ready -->
		<Project
			img="calcpy.gif"
			title="CalculatorPY"
			description="Calculator writen on Python. Very simple calculator for 2-3 actions, also has support function."
			buttonText="GitHub"
			href="https://github.com/coderpy4/calculatorPY" />
	</div>
</div>

<style lang="scss">
	@import '../../styles/mixins.scss';

	.grid {
		gap: 0.8rem;
		grid-auto-rows: 190px;
		justify-content: center;
		align-items: center;
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(350px, auto));
		width: min(90%, 72rem);

		@media screen and (max-width: 600px) {
			grid-auto-rows: 125px;
		}

		@media screen and (max-width: 868px) {
			width: min(100%, 75rem);
			gap: 0.2rem;
			grid-template-columns: 1fr 1fr 1fr;
		}

		&:before {
			@include outlineText($content: '&&', $translateX: -40%, $translateY: -160%);

			@media screen and (max-width: 868px) {
				@include outlineText($content: '&&', $translateX: -25%, $translateY: -95%);
			}
		}
	}

	.grid-container {
		display: flex;
		justify-content: center;
		margin-bottom: 4rem;
	}
</style>
