<script>
	import Social from '../atoms/Social.svelte';
	import { user } from '../../util/discord';
</script>

<div class="socials-container">
	<Social icon="github" tip="coderpy4" link="https://github.com/coderpy4" />
	<Social icon="discord" tip={user.username} link={`https://discord.com/users/${user.id}`} />
	<Social icon="email" tip="rosset.nocpes@skiff.com" link="mailto:rosset.nocpes@skiff.com" />
	<!--<Social icon="kofi" tip="" link="" />--> <!-- TODO Replace -->
</div>

<style>
	.socials-container {
		display: flex;
		gap: 0.75rem;
	}
</style>
