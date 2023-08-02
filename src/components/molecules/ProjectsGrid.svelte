<script>
	import Project from '../atoms/Project.svelte';
</script>

<div class="grid-container">
	<div class="grid">
		<Project img="stmc" type="png" title="Hello test" description="Nice MC server for friends and other people. We don't have any of the private chunks plugins. All building on the trust! Our Discord server: https://discord.gg/PqrYdYKhvm" />
		<Project img="calcpy" type="gif" title="CalculatorPY" description="Calculator writen on Python. Very simple calculator for 2-3 actions, also has support function." buttonText="Try it!" />
	</div>
</div>

<style lang="scss">
	@import '../../styles/mixins.scss';

	.grid {
		gap: 0.8rem;
		grid-auto-rows: 190px;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
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
