<script>
	import ProjectsGrid from '../molecules/ProjectsGrid.svelte';
	import Tooltip from '../atoms/Tooltip.svelte';
</script>

<section>
	<div class="wrapper" id="projects">
		<Tooltip tip="Click on an project">
			<h2><span>projects</span>:lol</h2>
		</Tooltip>
	</div>
	<ProjectsGrid />
</section>

<style lang="scss">
	span {
		color: var(--yellow);
	}

	h2 {
		display: inline-block;
		margin-bottom: 1rem;
	}

	div {
		display: flex;
		justify-content: center;
		margin-top: 0;

		@media (max-width: 868px) {
			justify-content: left;
			margin-bottom: 0.3rem;
		}
	}
</style>
